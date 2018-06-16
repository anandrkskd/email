#!/usr/bin/python3
import speech_recognition as sr 
def listen():                            #function to take voice input
# get audio from the microphone                                                                       
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")                
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)        #converting the text to speech
	print("                       "+text)   
        return text
    except sr.e:                #exception when audio not detected
        print("Fail to take input".format(e))
        
def audio(text):                       #function to convert text to speech
    import pyttsx3
    engine=pyttsx3.init()
    engine.say(text)           #text converted to speech form
    engine.runAndWait()        
        
def to_lower(raw_email_input):               #function to change upper case to lower case
    lower_case=raw_email_input.lower()
    email_id=lower_case.replace(" ", "")       #removing unwanted spaces 
    print("                          "+email_id)
    return email_id


text=listen()      
if 'send' in text :
    query="enter the receipient"       #taking the receiver as input
    print (q) 
    audio(q)                           #taking input through audio
    email_addr=listen()                #taking receiver mail address
    Receiver=to_lower(email_addr)      #processing the email address
    query1="Enter subject of the message"
    audio(q1)                       
    print (q1)
    subject_=listen()
    query2="Enter the content of the message"
    print (query2)
    audio(query2)
    content=listen()
    try:
        import email.message 
        import smtplib     #module to connect to email
        msg = email.message.Message()
        msg['Subject'] = subject_
        msg['From'] = "abhishek.yogi3105@gmail.com"
        msg['To'] = Receiver
        msg.add_header('Content-Type','text/html')
        msg.set_payload(content)
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587) #connecting to smtp server 
        smtp_server.starttls()                            #initiating a secure SMTP connection 
        smtp_server.login('abhishek.yogi3105@gmail.com', 'abhi8384')    
        smtp_server.sendmail(msg['From'], [msg['To']], msg.as_string())
        print('Messsage successfully sent')
    except sr.UnknownValueError:
        print("Could not send message")



