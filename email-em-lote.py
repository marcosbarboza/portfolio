from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import smtplib


def dispara(body_html, destination_email):
    # Server configuration
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('marcosjr861@gmail.com', 'mhsdwkjgyllrgget')

    # Sending Configuration
    msg = MIMEMultipart()
    msg['From'] = 'marcosjr861@gmail.com'
    msg['to'] = destination_email
    msg['Subject'] = "Teste Disparo de E-mail em lote"

    # Email body composition
    msg.attach(MIMEText(body_html, 'html'))

    # Sending
    server.send_message(msg)

    def prgreen(skk): print("\033[92m {}\033[00m".format(skk))
    prgreen('E-mail com link de compra -> Enviado')

    # Turn the server down
    server.quit()


def sendemail():
    # Data Input
    data_in = pd.read_excel('C:\\Users\\marco\\PycharmProjects\\Suporte-Teste-Automatizado\\teste-ip2.xlsx')

    # Creating arrays to save data
    key = []
    eleitor = []
    email = []

    # Saving the data in arrays
    for senha in data_in["KEY"]:
        key.append(senha)
    for eleitores in data_in["Nome"]:
        eleitor.append(eleitores)
    for emails in data_in["E-mail"]:
        email.append(emails)

    # Loop to load the specified data to compose the email body and destination for the email
    for envio in range(len(email)):
        nome = eleitor[envio]
        senha = key[envio]

        body = f"""<p align="justify"><span style="font-family: Calibri, serif;"><span style="font-size: medium;">Prezado (a) Associado(a),</span></span><span style="font-family: Calibri, serif;"><span style="font-size: medium;">&nbsp;</span></span><span style="font-family: Calibri, serif;"><span style="font-size: medium;">{nome}</span></span></p>
<p align="justify">&nbsp;</p>
<table style="height: 10px; width: 841px;">
<tbody>
<tr>
<td style="width: 835px; text-align: center;"><span style="font-size: medium;"><strong><span style="font-family: Calibri, serif;">SENHA PROVIS&Oacute;RIA</span></strong></span><span style="font-size: medium;"><span style="font-family: Calibri, serif;">:&nbsp;</span></span>
<h2><strong><span style="font-size: medium;"><span style="font-family: Calibri, serif;">{senha}</span></span></strong></h2>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<table style="width: 834px; height: 44px;">
<tbody>
<tr style="height: 22px;">
<td style="width: 824px; height: 22px; text-align: center;">
<h3><u><strong>Instru&ccedil;&otilde;es:</strong></u></h3>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p align="justify"><span style="font-family: Calibri, serif;"><span style="font-size: medium;"><em><br /><br /><br /><br /><br /><br /><br />O ambiente virtual de vota&ccedil;&atilde;o foi preparado pela empresa licitada Incorp Technology Inform&aacute;tica Ltda.&nbsp;</em></span></span></p>"""

        dest = email[envio]
        # Call the function with the specified properties
        dispara(body, dest)


sendemail()
