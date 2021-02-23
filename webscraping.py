import requests
from bs4 import BeautifulSoup
import smtplib
import time
from termcolor import cprint
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def catchnameprice(urllink, desiredprice, destination_email):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    monitoring = requests.get(urllink, headers=headers)

    soup = BeautifulSoup(monitoring.content, 'html.parser')
    product_name = soup.find(id="productTitle").get_text()
    catch_product_price = soup.find(id="price_inside_buybox").get_text()
    pre_convert_product_price = catch_product_price[2:]
    convert_product_price = pre_convert_product_price.replace(',', '.')
    convert_product_price_2 = convert_product_price.replace('$', '')
    product_price = float(convert_product_price_2)

    print(f'Produto: {product_name.strip()}')
    print(f'Preço Atual: R${product_price}')

    if product_price < desiredprice:

        body_html = f"""<html><head></head><body><h3><span style="font-family: Verdana, Geneva, sans-serif; color: rgb(0, 168, 133);">Seu produto chegou ao pre&ccedil;o esperado:</span></h3><p><a href="{urllink}" rel="noopener noreferrer" target="_blank">Clique aqui</a> para comprar</p></body></html>"""
        cprint('Preço Atingido', 'green')
        sendemail(body_html,destination_email)

    else:
        print('--------------------------------------------')
        cprint(f'Preço não alcaçado R${product_price}', 'red')


def sendemail(body_html,destination_email):
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
    msg['Subject'] = "Monitoramento"
    
    msg.attach(MIMEText(body_html, 'html'))
    
    # Sending
    server.send_message(msg)

    cprint('E-mail com link de compra -> Enviado', 'yellow')
    server.quit()


url = str(input('Insira o link para monitorar: '))
desired_price = float(input('Insira o valor desejado: '))
destination_email = str(input('Insira seu E-mail: '))

while True:
    catchnameprice(url, desired_price, destination_email)
    time.sleep(21600)
