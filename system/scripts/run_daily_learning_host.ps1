[CmdletBinding()]
param(
    [string]$ContainerName = "wiki-dev",
    [switch]$DryRun
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

try {
    Write-RunLog ("start=" + (Get-Date -Format o) + " container=" + $ContainerName + " dry_run=" + $DryRun)

    $running = (& docker inspect --format '{{.State.Running}}' $ContainerName 2>&1)
    if ($LASTEXITCODE -ne 0 -or ($running | Out-String).Trim() -ne "true") {
        Write-RunLog ("container-not-running=" + (($running | Out-String).Trim()))
        exit 75
    }

    & docker exec $ContainerName test -d /workspace/wiki
    if ($LASTEXITCODE -ne 0) {
        Write-RunLog "workspace-mount-check=failed"
        exit 75
    }

    $arguments = @(
        "exec", "--workdir", "/workspace/wiki", $ContainerName,
        "python3", "/workspace/wiki/system/scripts/run_daily_learning.py",
        "--root", "/workspace/wiki", "--day-index", "auto", "--mode", "daily-learning"
    )
    if ($DryRun) { $arguments += "--dry-run" }

    Write-RunLog ("command=docker " + ($arguments -join " "))
    & docker @arguments 2>&1 | Tee-Object -FilePath $LogPath -Append
    $exitCode = $LASTEXITCODE
    Write-RunLog ("exit=" + $exitCode + " end=" + (Get-Date -Format o))
    exit $exitCode
}
catch {
    Write-RunLog ("wrapper-error=" + $_.Exception.Message)
    exit 2
}
