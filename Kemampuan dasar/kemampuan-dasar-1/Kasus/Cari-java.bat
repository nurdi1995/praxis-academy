Get-ChildItem *.bat
if (Get-ChildItem){
Write-Host("ada file di ")
}
else {
Write-Host("Tidak ada file")
}