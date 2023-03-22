"""a ferramenta ainda esta enviando email a um grupo de emails permitidos ainda"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações de e-mail
de_email = 'lucas.iglesias02@gmail.com'
de_senha = 'fzkezsexnkxhxstx'
assunto = 'seu gay'
mensagem = 'me mama'

# Grupos de e-mails permitidos
grupos_permitidos = {
    'rh': ['matheussantanas617@gmail.com', 'vacsonsbanison@gmail.com'],
    'suporte': ['m3s2teste@gmail.com', 'coisafgd@gmail.com'],
    'marketing': ['luthi381@gmail.com', 'lucas@empresa.com']
}

# Solicitar nome do grupo
grupo = input('Digite o nome do grupo para enviar a mensagem (rh, suporte, marketing): ')

# Verificar se o grupo é permitido
if grupo not in grupos_permitidos:
    print(f'O grupo {grupo} não é permitido.')
else:
    # Construir lista de destinatários
    para_emails = grupos_permitidos[grupo]

    # Construir mensagem
    msg = MIMEMultipart()
    msg['From'] = de_email
    msg['To'] = ', '.join(para_emails)
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    # Conectar ao servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(de_email, de_senha)

    try:
        # Enviar mensagem
        smtp.sendmail(de_email, para_emails, msg.as_string())
    except Exception as e:
        print('Erro ao enviar e-mail: ' + str(e))
    finally:
        smtp.quit()

    print('E-mail enviado com sucesso.')
    
