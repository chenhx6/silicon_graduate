[CmdletBinding()]
param(
    [string]$TaskName = "SiliconGraduate-Wiki-DailyLearning",
    [string]$WrapperPath = ""
)

$ErrorActionPreference = "Stop"
if ([string]::IsNullOrWhiteSpace($WrapperPath)) {
    $WrapperPath = Join-Path $PSScriptRoot "run_daily_learning_host.ps1"
}
if (-not (Test-Path -LiteralPath $WrapperPath -PathType Leaf)) {
    throw "Wrapper script not found: $WrapperPath"
}

$HostTimeZone = (Get-TimeZone).Id
Write-Host ("Host timezone: " + $HostTimeZone + ". The trigger is 22:00 in the host's local timezone; use China Standard Time for Asia/Shanghai semantics.")

$PowerShell = (Get-Command powershell.exe -ErrorAction Stop).Source
$QuotedWrapper = '"' + $WrapperPath + '"'
$Action = New-ScheduledTaskAction -Execute $PowerShell -Argument ("-NoProfile -ExecutionPolicy Bypass -File " + $QuotedWrapper)
$Trigger = New-ScheduledTaskTrigger -Daily -At ([datetime]::Today.AddHours(22))
$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Hours 12)

if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    throw "Task already exists: $TaskName. Inspect it before changing it; this script never overwrites an existing task."
}

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Description "Run the Docker-hosted Wiki one-month nuclear-structure learning runner at 22:00 Asia/Shanghai." `
    -User $env:USERNAME `
    -RunLevel Limited | Out-Host

Write-Host "Registered $TaskName. Verify the Windows task timezone and run history before counting Day 1."
