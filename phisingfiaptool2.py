import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# configurações de e-mail
de_email = ''
de_senha = "''
para_email = ''
assunto = 'teste'
mensagem = 'teste'

# construir mensagem
msg = MIMEMultipart()
msg['From'] = de_email
msg['To'] = para_email
msg['Subject'] = assunto
msg.attach(MIMEText(mensagem, 'plain'))

# conectar ao servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
smtp.login(de_email, de_senha)

try:
    # enviar mensagem
    smtp.sendmail(de_email, para_email, msg.as_string())
except Exception as e:
    print('Erro ao enviar e-mail: ' + str(e))
finally:
    smtp.quit()

print('E-mail enviado com sucesso.')
