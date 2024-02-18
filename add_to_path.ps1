# Add current script's directory to PATH environment variable if not already present
$scriptPath = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")

if (-not $userPath.Split(';').Contains($scriptPath)) {
    $newUserPath = "$userPath;$scriptPath"
    [Environment]::SetEnvironmentVariable("PATH", $newUserPath, "User")
    Write-Host "The directory has been added to your PATH. Please restart your terminal."
} else {
    Write-Host "The directory is already in your PATH."
}

# Function to run gpt.py with any passed arguments
function Run-Gpt {
    param (
        [string[]]$Args
    )

    $gptPyPath = Join-Path -Path $scriptPath -ChildPath "gpt.py"
    $pythonCommand = "python `"$gptPyPath`" $($Args -join ' ')"
    Invoke-Expression $pythonCommand
}