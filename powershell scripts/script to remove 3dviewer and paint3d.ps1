# Powershell script for removing 3D Viewer and Paint 3D from a computer
# Some packages are hard-coded. Update as necessary.

Write-Host "Removing provisioned package for 3D Viewer"
try {Remove-AppxProvisionedPackage -Online -PackageName Microsoft.Microsoft3DViewer_2021.2105.4012.0_neutral_~_8wekyb3d8bbwe}
catch {"==Provisioned package for 3D Viewer not found.=="}

Write-Host "Removing provisioned package for Paint 3D"
try {Remove-AppxProvisionedPackage -Online -PackageName Microsoft.MSPaint_2021.2105.4017.0_neutral_~_8wekyb3d8bbwe}
catch {"==Provisioned package for Paint 3D not found.=="}

Write-Host "Removing user package for 3D Viewer"
try {Get-AppxPackage -allusers *3dviewer* | Remove-AppxPackage -allusers}
catch {"==3D Viewer local app not found.=="}

Write-Host "Removing user package for Paint 3D"
try {Get-AppxPackage -allusers *paint* | Remove-AppxPackage -allusers}
catch {"==3D Viewer local app not found.=="}

# Check for any remaining apps
Write-Host "Final Checks"
Get-AppxProvisionedPackage -online | Where-Object {$_.displayname -Like "*3dviewer*"}
Get-AppxProvisionedPackage -online | Where-Object {$_.displayname -Like "*paint*"}
Get-AppxPackage -AllUsers | select name, packagefullname | Where-Object {$_.name -Like "*3dviewer*"}
Get-AppxPackage -AllUsers | select name, packagefullname | Where-Object {$_.name -Like "*paint*"}