#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import smtplib
from time import sleep
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys

if len (sys.argv) != 7:
    print "Usage: e-mail_multiprocessado.py [e-mail de origem] [senha do e-mail] [e-mail de destino] [assunto do e-mail] [corpo do e-mail] [Quantidade de e-mail]"
    sys.exit (1)

fromaddr = sys.argv[1]
senha = sys.argv[2]
toaddr = sys.argv[3]
assunto_do_email = sys.argv[4]
corpo_do_email = sys.argv[5]
quantidade=int(sys.argv[6])

def envia(fromaddr,senha,toaddr,assunto_do_email,corpo_do_email):
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = str(assunto_do_email)
	msg.attach(MIMEText(corpo_do_email, 'plain'))
	server = smtplib.SMTP('servidor_smtp', 587)
	server.starttls()
	server.login(fromaddr, senha)
	text = msg.as_string()
	try:
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		print ('E-mail enviado OK')
	except smtplib.SMTPException as error:
		print error

processes = []

for m in range(quantidade):
   n = m + 1
   p = Process(target=envia, args=( fromaddr,senha,toaddr,assunto_do_email,corpo_do_email ))
   p.start()
   processes.append(p)

for p in processes:
   try:
   	p.join()
   except:
   	print 'error'
