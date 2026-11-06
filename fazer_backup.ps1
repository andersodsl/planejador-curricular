
$ErrorActionPreference = "Stop"

# Caminho do executável do SurrealDB
$SurrealExe = Join-Path $env:LOCALAPPDATA "SurrealDB\surreal.exe"

# Pasta onde os backups serão armazenados
$BackupDir = Join-Path $PSScriptRoot "backups"

# Verifica se o executável existe
if (-not (Test-Path $SurrealExe)) {
    Write-Host "Erro: executável do SurrealDB não encontrado."
    exit 1
}

# Cria a pasta de backups, caso não exista
New-Item -ItemType Directory -Force -Path $BackupDir | Out-Null

# Gera nome com data e horário
$Data = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$BackupFile = Join-Path $BackupDir "backup_$Data.surql"

Write-Host "Iniciando backup do banco..."

# Executa a exportação
& $SurrealExe db export `
    --endpoint "http://127.0.0.1:8001" `
    --username root `
    --password root `
    --namespace planejador_curricular `
    --database planejador_curricular `
    $BackupFile

# Verifica se a exportação foi concluída
if ($LASTEXITCODE -ne 0) {
    Write-Host "Erro ao gerar o backup."
    exit 1
}

if (Test-Path $BackupFile) {
    Write-Host ""
    Write-Host "Backup realizado com sucesso!"
    Write-Host "Arquivo: $BackupFile"
} else {
    Write-Host "Erro: arquivo de backup não encontrado."
    exit 1
}
