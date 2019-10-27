import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Systemkamera-Klapp-Display-Echtzeit-Autofokus-AF-Punkten/dp/B07MWDKNGN/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=camera&qid=1572168842&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQjJTTkVZM0Q2M1U4JmVuY3J5cHRlZElkPUEwMTgzNzQyMk04MlI1R1c3SFlIRSZlbmNyeXB0ZWRBZElkPUEwODU0NTE3SEpIVDRVUTVJS1dLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    convert_price = float(price[0:3])


    if(convert_price < 1000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('perfect.igbadumhe@gmail.com', 'password_password')

    subject = 'Price is DOWN!!!!'
    body = 'check the amazon link: https://www.amazon.de/Sony-Systemkamera-Klapp-Display-Echtzeit-Autofokus-AF-Punkten/dp/B07MWDKNGN/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=camera&qid=1572168842&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQjJTTkVZM0Q2M1U4JmVuY3J5cHRlZElkPUEwMTgzNzQyMk04MlI1R1c3SFlIRSZlbmNyeXB0ZWRBZElkPUEwODU0NTE3SEpIVDRVUTVJS1dLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'perfect.igbadumhe@gmail.com',
        'graphicdojo442@gmail.com',

        msg
    )
    print('Hey Email has been sent')
    server.quit()

while(True):
    check_price()
    time.sleep(120*10)
