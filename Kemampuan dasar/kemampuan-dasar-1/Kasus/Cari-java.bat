Get-ChildItem *.bat

$Data1=Get-ChildItem

if ($Data1 -eq Get-ChildItem){
Write-Host("ada file")
}
else {
Write-Host("Tidak ada file")
}