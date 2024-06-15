import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Defina suas credenciais de login
email = 'frederico.almeida@grupomulti.com.br'
password = 'Senha aqui'

# Crie uma conexão SMTP com o servidor do Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Faça login na sua conta do Gmail
server.login(email, password)

# Defina os parâmetros do e-mail
from_email = email
to_email = 'frederico.almeida@grupomulti.com.br, robson.silva@grupomulti.com.br'
subject = 'NÃO FIQUE DE FORA!'
body = 'Ultimos ingressos'

for i in range (1):
    # Crie a mensagem do e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adicione o corpo do e-mail
    msg.attach(MIMEText(body, 'plain'))

    # Abra a imagem a ser anexada
    with open('C:/Users/frederico.almeida\PycharmProjects/testes/famoso.jpg', 'rb') as f:
        img = MIMEImage(f.read())

    # Adicione a imagem como anexo
    img.add_header('Content-Disposition', 'attachment', filename='imagem.jpg')
    msg.attach(img)

    # Envie o e-mail
    server.sendmail(from_email, to_email.split(','), msg.as_string())

# Feche a conexão SMTP
server.quit()

print('E-mail enviado com sucesso!')
