import requests
from bs4 import BeautifulSoup
import smtplib
import time
from termcolor import cprint


def catchnameprice(urllink, desiredprice):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}

    monitoring = requests.get(urllink, headers=headers)

    soup = BeautifulSoup(monitoring.content, 'html.parser')
    product_name = soup.find(id="productTitle").get_text()
    catch_product_price = soup.find(id="priceblock_ourprice").get_text()
    pre_convert_product_price = catch_product_price[2:]
    convert_product_price = pre_convert_product_price.replace(',', '.')
    product_price = float(convert_product_price)

    print(f'Produto: {product_name.strip()}')
    print(f'Preço Atual: R${product_price}')

    if product_price < desiredprice:
        subject = 'O Preco Abaixou !'.encode('ISO-8859-1')
        body = f'Para comprar o \n{product_name.strip()}, \nAcesse: {urllink}'.encode('ISO-8859-1')
        cprint('Preço Atingido', 'green')
        sendemail(subject, body)

    else:
        print('--------------------------------------------')
        cprint(f'Preço não alcaçado R${product_price}', 'red')


def sendemail(subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('marcosjr861@gmail.com', 'mhsdwkjgyllrgget')

    subject = subject
    body = body
    msg = f"Subject: {subject}\n\n{body}".encode('ISO-8859-1')

    server.sendmail(
        'marcosjr861@gmail.com',
        'marcosjr861@gmail.com',
        msg
    )
    cprint('E-mail com link de compra -> Enviado', 'yellow')
    server.quit()


url = str(input('Insira o link para monitorar: '))
desired_price = float(input('Insira o valor desejado: '))

while True:
    catchnameprice(url, desired_price)
    time.sleep(21600)
