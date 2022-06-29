import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email_anexo(corpo, destino, assunto, anexo):
    try:
        fromaddr = "ricardoautomacoes@gmail.com"
        toaddr = destino
        msg = MIMEMultipart()


        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "AUTOMACAO -> " + assunto

        body = "\n" + corpo

        msg.attach(MIMEText(body, 'plain'))

        filename = anexo

        attachment = open(anexo,'rb')


        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "Ca@34512516")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        return "1"

    except:

        return "0"