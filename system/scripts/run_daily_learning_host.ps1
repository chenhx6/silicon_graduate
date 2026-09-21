[CmdletBinding()]
param(
    [string]$ContainerName = "wiki-dev",
    [switch]$DryRun,
    [int]$MaxAttempts = 4
)

$ErrorActionPreference = "Stop"
$LogRoot = Join-Path $env:LOCALAPPDATA "silicon-graduate\wiki-daily-learning"
$null = New-Item -ItemType Directory -Force -Path $LogRoot
$RunStamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$LogPath = Join-Path $LogRoot ("host-run-" + $RunStamp + ".log")

function Write-RunLog {
    param([string]$Message)
    $Message | Tee-Object -FilePath $LogPath -Append
}

function Wait-ContainerReady {
    param([int]$Attempt)
    $running = (& docker inspect --format '{{.State.Running}}' $ContainerName 2>&1)
    if ($LASTEXITCODE -ne 0 -or ($running | Out-String).Trim() -ne "true") {
        Write-RunLog ("attempt=" + $Attempt + " container-not-ready=" + (($running | Out-String).Trim()))
        return $false
    }
    & docker exec $ContainerName test -d /workspace/wiki
    if ($LASTEXITCODE -ne 0) {
        Write-RunLog ("attempt=" + $Attempt + " workspace-mount-check=failed")
        return $false
    }
    & docker exec $ContainerName test -x /usr/bin/python3
    if ($LASTEXITCODE -ne 0) {
        Write-RunLog ("attempt=" + $Attempt + " python-check=failed")
        return $false
    }
    return $true
}

try {
    Write-RunLog ("start=" + (Get-Date -Format o) + " container=" + $ContainerName + " dry_run=" + $DryRun)

    $arguments = @(
        "exec", "--workdir", "/workspace/wiki", $ContainerName,
        "python3", "/workspace/wiki/system/scripts/run_daily_learning.py",
        "--root", "/workspace/wiki", "--day-index", "auto", "--mode", "daily-learning"
    )
    if ($DryRun) { $arguments += "--dry-run" }

    $retryDelays = @(60, 180, 600)
    for ($attempt = 1; $attempt -le $MaxAttempts; $attempt++) {
        if (-not (Wait-ContainerReady -Attempt $attempt)) {
            if ($attempt -lt $MaxAttempts) {
                $delay = $retryDelays[[Math]::Min($attempt - 1, $retryDelays.Count - 1)]
                Write-RunLog ("retry-after-seconds=" + $delay)
                Start-Sleep -Seconds $delay
                continue
            }
            Write-RunLog ("container-readiness-failed attempts=" + $MaxAttempts)
            exit 75
        }

        Write-RunLog ("attempt=" + $attempt + " command=docker " + ($arguments -join " "))
        $output = @(& docker @arguments 2>&1)
        $output | Tee-Object -FilePath $LogPath -Append | Out-Host
        $exitCode = $LASTEXITCODE
        Write-RunLog ("attempt=" + $attempt + " exit=" + $exitCode)

        # 75/125/126/127 and daemon/startup messages are retryable. A runner
        # preflight failure (3) or scientific verification failure (1) is not.
        $joined = ($output | Out-String)
        $retryable = ($exitCode -in @(75, 125, 126, 127)) -or ($joined -match "Cannot connect to the Docker daemon|container .* is not running|permission denied")
        if ($exitCode -eq 0 -or -not $retryable -or $attempt -ge $MaxAttempts) {
            Write-RunLog ("final-exit=" + $exitCode + " end=" + (Get-Date -Format o))
            exit $exitCode
        }
        $delay = $retryDelays[[Math]::Min($attempt - 1, $retryDelays.Count - 1)]
        Write-RunLog ("retryable-failure retry-after-seconds=" + $delay)
        Start-Sleep -Seconds $delay
    }
    exit 75
}
catch {
    Write-RunLog ("wrapper-error=" + $_.Exception.Message)
    exit 2
}
