import argparse
import os
import smtplib

# Configurações de e-mail
email_de = "seuemail@dominio.com"
senha = "sua_senha_do_email"

# Lista de e-mails permitidos
lista_de_emails_permitidos = ["email1@dominio.com", "email2@dominio.com", "email3@dominio.com"]

# Função para enviar e-mails
def enviar_email(email, modelo):
    # Substituir variáveis no modelo de e-mail
    with open(modelo, "r") as f:
        mensagem = f.read().replace("NOME_DO_DESTINATARIO", email)

    # Enviar e-mail
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_de, senha)
        server.sendmail(email_de, email, mensagem)
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar e-mail para {email}: {e}")
    else:
        print(f"E-mail enviado com sucesso para {email}!")

# Configurar argparse
parser = argparse.ArgumentParser(description="Envia e-mails para uma lista de usuários.")
parser.add_argument("-a", "--adicionar", nargs=2, metavar=("TIPO", "NOME"), help="Adicionar um novo modelo de e-mail ou um novo usuário.")
parser.add_argument("-t", "--template", help="Modelo de e-mail a ser enviado.")
parser.add_argument("--to", required=True, help="E-mail do destinatário.")
parser.add_argument("--recipients", nargs="+", required=True, help="Lista de usuários para os quais o e-mail será enviado.")

# Verificar argumentos do argparse
args = parser.parse_args()

if args.adicionar:
    tipo = args.adicionar[0]
    nome = args.adicionar[1]
    if tipo == "modelo":
        with open(nome, "w") as f:
            f.write("Olá NOME_DO_DESTINATARIO, este é um exemplo de modelo de e-mail.")
        print(f"Modelo de e-mail {nome} adicionado com sucesso!")
    elif tipo == "usuario":
        if nome in lista_de_emails_permitidos:
            print(f"O usuário {nome} já está na lista de e-mails permitidos.")
        else:
            lista_de_emails_permitidos.append(nome)
            print(f"Usuário {nome} adicionado à lista de e-mails permitidos.")
    else:
        print(f"Tipo {tipo} inválido. Use 'modelo' ou 'usuario'.")
    exit()

if not args.template:
    print("É necessário informar o modelo de e-mail a ser enviado.")
    exit()

if not os.path.isfile(args.template):
    print("Arquivo do modelo não encontrado. Saindo...")
    exit(1)

# Verificar se todos os destinatários são permitidos
for email in args.recipients:
    if email not in lista_de_emails_permitidos:
        print(f"Usuário {email} não está autorizado a receber e-mails.")
        exit(1)

# Loop através da lista de e-mails
for email in args.recipients:
    enviar_email(email, args.template)

print("E-mails enviados com sucesso!")
