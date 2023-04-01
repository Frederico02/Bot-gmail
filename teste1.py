import smtplib

# Defina suas credenciais de login
email = 'frederico.almeida@grupomulti.com.br'
password = '*********'

# Crie uma conexão SMTP com o servidor do Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

# Faça login na sua conta do Gmail
server.login(email, password)

# Defina os parâmetros do e-mail
from_email = email
to_email = 'robson.silva@grupomulti.com.br'
subject = 'teste'
body = 'Corpo do e-mail'

# Crie a mensagem do e-mail
message = f'Subject: {subject}\n\n{body}'

# Envie o e-mail
server.sendmail(from_email, to_email, message)

# Feche a conexão SMTP
server.quit()

print('E-mail enviado com sucesso!')
