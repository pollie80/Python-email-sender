# pip install quick-mailer
# This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..)
from mailer import Mailer

f = open('content.txt', 'r')
content = f.read()
f.close()

mail = Mailer(email='<senderemail>', password='<password>')
mail.send(receiver='<receiveremail>', subject='Message from a Python program hehe', message=content)