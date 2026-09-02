$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
Set-Location $RepoRoot
python scripts/automation/run_all.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
