# Configuración del servidor SMTP
$SmtpServer = "smtp.gmail.com"
$SmtpPort = 587
$Username = "kevincuellararias994@gmail.com"

# IMPORTANTE: Cambia esta contraseña por una nueva (la actual está comprometida)
# Genera una nueva en: https://myaccount.google.com/apppasswords
$Password = "vdnsqbgiggigfbzd"  # Sin espacios

# Convertir contraseña a SecureString para mayor seguridad
$SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force

# Crear el objeto de correo
$Mail = New-Object System.Net.Mail.MailMessage
$Mail.From = $Username
$Mail.To.Add("mariano.gail@gmail.com")
$Mail.Subject = "Correo enviado desde PowerShell"
$Mail.Body = "Este es el contenido del correo electrónico enviado desde PowerShell, ATT: Kevin"

# Crear cliente SMTP
$Smtp = New-Object System.Net.Mail.SmtpClient($SmtpServer, $SmtpPort)
$Smtp.EnableSsl = $true
$Smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $SecurePassword)

# Enviar el correo
try {
    $Smtp.Send($Mail)
    Write-Host "Correo enviado exitosamente" -ForegroundColor Green
}
catch {
    Write-Host "Error al enviar el correo: $_" -ForegroundColor Red
}
finally {
    # Liberar recursos
    if ($Mail) { $Mail.Dispose() }
    if ($Smtp) { $Smtp.Dispose() }
}
