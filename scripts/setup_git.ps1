# Parse the conf.ini file
$iniContent = Get-Content -Path 'config/conf.ini' -Raw
$gitSection = ($iniContent -split '\n\n' | Where-Object { $_ -match '^\[git\]' }) -split '\n' | Select-Object -Skip 1
$username = ($gitSection | Where-Object { $_ -match '^username' }).Split('=')[1].Trim()
$repo_name = ($gitSection | Where-Object { $_ -match '^repo_name' }).Split('=')[1].Trim()

# Check if git has already been initialized
if (Test-Path .git) {
    Write-Host "Git has already been initialized in this directory."
} else {
    # Use the extracted values
    Add-Content -Path README.md -Value "# $repo_name"
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin "https://github.com/$username/$repo_name.git"
    git push -u origin main
}
