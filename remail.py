import smtplib
import email


def enviar_email(corpo, destino, assunto):
    # anexo

    corpo_email = "\n" + corpo
    msg = email.message.Message()
    msg['Subject'] = "AUTOMACAO -> " + assunto
    msg['From'] = "ricardoautomacoes@gmail.com"
    msg['To'] = destino
    password = 'Ca@34512516'
    msg.add_header('Content - Type', 'text / html')
    msg.set_payload(corpo_email)


    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    #print('Email enviado')