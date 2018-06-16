import imaplib
import email
from bs4 import BeautifulSoup
import speech_recognition as sr
import os
import mimetypes


mail= imaplib.IMAP4_SSL ("imap.gmail.com",993)

unm='abhishekyogi833@gmail.com'
pwd='abhi8384'

mail.login(unm,pwd)




	
def save_file():
	save_path=os.path.join(os.getcwd(),'emails',date_,subject_)
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	with open(os.path.join(save_path, filename),'wb')as fp:
		fp.write(part.get_payload(decode=True))
	return save_path	

def listen():
	# get audio from the microphone                                                                       
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Goto?")
		audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print("                       "+text)
		return text
	except sr.RequestError as e:
		print("NNN;[0]".format(e))
def goto():
	text=listen()
	if 'inbox' in text :
		query='Inbox'
	elif 'Trash' in text:
		query='Trash'
	elif 'Outbox' in text:
		query=''"[Gmail]/Sent Mail"''
	elif 'Star' in text:
		query=''"[Gmail]/Starred"''
	elif 'Important' in text:
		query=''"[Gmail]/Important"''
	elif 'Spam' in text:
		query=''"[Gmail]/Spam"''
	elif 'Drafts' in text:
		query=''"[Gmail]/Drafts"''
	elif 'All' in text:
		query=''"[Gmail]/All Mail"''



mail.select(query)
print("You have entered your "+query)
result,data=mail.uid('search',None,"ALL")
inbox_item_list= data[0].split()
most_recent=inbox_item_list[-1]
oldest=inbox_item_list[0]
for item in most_recent:
	result2, email_data=mail.uid('fetch',most_recent,'(RFC822)')
	raw_email=email_data[0][1].decode("utf-8")
	email_message=email.message_from_string(raw_email)
	to_=email_message['To']
	from_=email_message['From']
	subject_=email_message['Subject']
	date_=email_message['date']
	counter=1

	for part in email_message.walk():
		if part.get_content_maintype()=='multipart':
			continue
		filename=part.get_filename()
		content_type=part.get_content_type()
		if not filename:
			ext= mimetypes.guess_extension(part.get_content_type())
			if not ext:
				ext= '.bin'
			filename='msg-part-%08d%s' %(counter, ext)

	counter+=1
	if'plain' in content_type:
		print(part.get_payload())
		location=save_file()
	elif 'html' in content_type:
		html_= part.get_payload()
		soup= BeautifulSoup(html_,'html.parser')
		text=soup.get_text()
		print (subject_)
		print(text)
		location=save_file()
	else:
		print ("Unknown type")

	print(content_type)
		

	
email_message.get_payload()
def read():
	import pyttsx3
	voiceEngine = pyttsx3.init()
	 
	rate = voiceEngine.getProperty('rate')
	volume = voiceEngine.getProperty('volume')
	voice = voiceEngine.getProperty('voice')
	 
	print (rate)
	print (volume)
	print (voice)
	try:
		infile =location+'/'+filename
	 
		newVoiceRate = 50
		while newVoiceRate <= 300:
			voiceEngine.setProperty('rate', newVoiceRate)
			f = open(infile, 'r')
			theText = f.read()
			f.close()
			voiceEngine.say(theText)
			voiceEngine.runAndWait()
			newVoiceRate = newVoiceRate+50
			voiceEngine.setProperty('rate', 125)

	except :
		print("Cannot read file")
read()


