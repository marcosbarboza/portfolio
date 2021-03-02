import time
from termcolor import cprint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

breaker = 0


def getinfoproductamazon(desired_price, user_email_in, url):
    options = Options()
    options.headless = True
    cprint('# --- Iniciando Consulta --- #', 'yellow')
    drive = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
    drive.get(url)

    cprint('->> Checando Produto ✓', 'blue')
    get_product_name = drive.find_element_by_xpath('//*[@id="productTitle"]').text
    get_product_price = drive.find_element_by_xpath('//*[@id="price_inside_buybox"]').text
    product_price = float(get_product_price.strip('R$').replace(',', '.'))
    target_price = float(desired_price)

    if product_price <= target_price:
        cprint('->> Preço Atingido ✓', 'blue')
        email_body = '<!doctype html><html> <head> <meta name="viewport" content="width=device-width" /> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> <title>Simple Transactional Email</title> <style> /* ------------------------------------- GLOBAL RESETS ------------------------------------- */ /*All the styling goes here*/ img { border: none; -ms-interpolation-mode: bicubic; max-width: 100%; } body { background-color: #f6f6f6; font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; } table { border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; } table td { font-family: sans-serif; font-size: 14px; vertical-align: top; } /* ------------------------------------- BODY & CONTAINER ------------------------------------- */ .body { background-color: #f6f6f6; width: 100%; } /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */ .container { display: block; margin: 0 auto !important; /* makes it centered */ max-width: 580px; padding: 10px; width: 580px; } /* This should also be a block element, so that it will fill 100% of the .container */ .content { box-sizing: border-box; display: block; margin: 0 auto; max-width: 580px; padding: 10px; } /* ------------------------------------- HEADER, FOOTER, MAIN ------------------------------------- */ .main { background: #ffffff; border-radius: 3px; width: 100%; } .wrapper { box-sizing: border-box; padding: 20px; } .content-block { padding-bottom: 10px; padding-top: 10px; } .footer { clear: both; margin-top: 10px; text-align: center; width: 100%; } .footer td, .footer p, .footer span, .footer a { color: #999999; font-size: 12px; text-align: center; } /* ------------------------------------- TYPOGRAPHY ------------------------------------- */ h1, h2, h3, h4 { color: #000000; font-family: sans-serif; font-weight: 400; line-height: 1.4; margin: 0; margin-bottom: 30px; } h1 { font-size: 35px; font-weight: 300; text-align: center; text-transform: capitalize; } p, ul, ol { font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px; } p li, ul li, ol li { list-style-position: inside; margin-left: 5px; } a { color: #3498db; text-decoration: underline; } /* ------------------------------------- BUTTONS ------------------------------------- */ .btn { box-sizing: border-box; width: 100%; } .btn > tbody > tr > td { padding-bottom: 15px; } .btn table { width: auto; } .btn table td { background-color: #ffffff; border-radius: 5px; text-align: center; } .btn a { background-color: #ffffff; border: solid 1px #3498db; border-radius: 5px; box-sizing: border-box; color: #3498db; cursor: pointer; display: inline-block; font-size: 14px; font-weight: bold; margin: 0; padding: 12px 25px; text-decoration: none; text-transform: capitalize; } .btn-primary table td { background-color: #3498db; } .btn-primary a { background-color: #3498db; border-color: #3498db; color: #ffffff; } /* ------------------------------------- OTHER STYLES THAT MIGHT BE USEFUL ------------------------------------- */ .last { margin-bottom: 0; } .first { margin-top: 0; } .align-center { text-align: center; } .align-right { text-align: right; } .align-left { text-align: left; } .clear { clear: both; } .mt0 { margin-top: 0; } .mb0 { margin-bottom: 0; } .preheader { color: transparent; display: none; height: 0; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all; visibility: hidden; width: 0; } .powered-by a { text-decoration: none; } hr { border: 0; border-bottom: 1px solid #f6f6f6; margin: 20px 0; } /* ------------------------------------- RESPONSIVE AND MOBILE FRIENDLY STYLES ------------------------------------- */ @media only screen and (max-width: 620px) { table[class=body] h1 { font-size: 28px !important; margin-bottom: 10px !important; } table[class=body] p, table[class=body] ul, table[class=body] ol, table[class=body] td, table[class=body] span, table[class=body] a { font-size: 16px !important; } table[class=body] .wrapper, table[class=body] .article { padding: 10px !important; } table[class=body] .content { padding: 0 !important; } table[class=body] .container { padding: 0 !important; width: 100% !important; } table[class=body] .main { border-left-width: 0 !important; border-radius: 0 !important; border-right-width: 0 !important; } table[class=body] .btn table { width: 100% !important; } table[class=body] .btn a { width: 100% !important; } table[class=body] .img-responsive { height: auto !important; max-width: 100% !important; width: auto !important; } } /* ------------------------------------- PRESERVE THESE STYLES IN THE HEAD ------------------------------------- */ @media all { .ExternalClass { width: 100%; } .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div { line-height: 100%; } .apple-link a { color: inherit !important; font-family: inherit !important; font-size: inherit !important; font-weight: inherit !important; line-height: inherit !important; text-decoration: none !important; } #MessageViewBody a { color: inherit; text-decoration: none; font-size: inherit; font-family: inherit; font-weight: inherit; line-height: inherit; } .btn-primary table td:hover { background-color: #34495e !important; } .btn-primary a:hover { background-color: #34495e !important; border-color: #34495e !important; } } </style> </head> <body class=""> <span class="preheader">Seu produto chegou ao preço desejado.</span> <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body"> <tr> <td>&nbsp;</td> <td class="container"> <div class="content"> <!-- START CENTERED WHITE CONTAINER --> <table role="presentation" class="main"> <!-- START MAIN CONTENT AREA --> <tr> <td class="wrapper"> <table role="presentation" border="0" cellpadding="0" cellspacing="0"> <tr> <td> <p>MEG - Comparador de preços,</p> <p>O produto que você escolheu rastrear chegou ao preço desejado</p> <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary"> <tbody> <tr> <td align="left"> <table role="presentation" border="0" cellpadding="0" cellspacing="0"> <tbody> <tr> <td> <a href="%url_link%" target="_blank">Comprar</a> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <p>Produto: %get_product_name%</p> <p>Preço: %get_product_price%</p> <p>Boas Compras.</p> </td> </tr> </table> </td> </tr> <!-- END MAIN CONTENT AREA --> </table> <!-- END CENTERED WHITE CONTAINER --> <!-- START FOOTER --> <div class="footer"> <table role="presentation" border="0" cellpadding="0" cellspacing="0"> <tr> <td class="content-block"> <span class="apple-link">MEG Technologys and Design</span> <br> Sistema de Comparação de Preços <a href="https://megrecomenda.com">Acesse</a>. </td> </tr> <tr> <td class="content-block powered-by"> Powered by <a href="https://megrecomenda.com">SEG4 - MEG Technologys</a>. </td> </tr> </table> </div> <!-- END FOOTER --> </div> </td> <td>&nbsp;</td> </tr> </table> </body></html>'
        format_email_body = email_body.replace('%get_product_name%', get_product_name).replace('%get_product_price%',
                                                                                               get_product_price).replace(
            '%url_link%', url)
        sendemail(user_email_in, format_email_body)
    else:
        cprint('->> Preço não atingido X', 'red')
        print(f'->> Preço Atual: {get_product_price}')


def sendemail(destination_email, body_html):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    # Server configuration
    cprint('->> Enviando e-mail - Iniciando Servidor SMTP ✓', 'blue')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('marcosjr861@gmail.com', 'mhsdwkjgyllrgget')
    # Sending Configuration

    cprint('->> Carregando Path de e-mail ✓', 'blue')
    msg = MIMEMultipart()
    msg['From'] = 'marcosjr861@gmail.com'
    msg['to'] = destination_email
    msg['Subject'] = "Monitoramento"

    msg.attach(MIMEText(body_html, 'html'))

    # Sending
    cprint('->> Disparando e-mail', 'yellow')
    server.send_message(msg)

    cprint('E-mail com link de compra -> Enviado ✓', 'green')
    server.quit()
    global breaker
    breaker = 1


# url_link = str(input('Insira o link para monitorar: '))
# user_price = float(input('Preço desejado: '))
# user_email = str(input('Insira o email para ser avisado: '))

url_link = 'https://www.amazon.com.br/Teclado-Mec%C3%A2nico-Lightspeed-Logitech-Teclados/dp/B07GPRXZQF/ref=pd_bxgy_img_2/143-1782934-6089750?_encoding=UTF8&pd_rd_i=B07GPRXZQF&pd_rd_r=f90e85f0-d0eb-44f3-8505-9fddda6b4c79&pd_rd_w=3XLMK&pd_rd_wg=Labjc&pf_rd_p=400138fd-99e3-44de-aed2-5a7aff7ca010&pf_rd_r=J22RQM72PFE1Q5KN27NW&psc=1&refRID=J22RQM72PFE1Q5KN27NW'
user_price = float('680.1')
user_email = str('marcosjr861@gmail.com')

if __name__ == '__main__':
    while True:
        if breaker == 0:
            getinfoproductamazon(user_price, user_email, url_link)
            time.sleep(1800)
        else:
            break
