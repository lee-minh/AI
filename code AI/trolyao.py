import speech_recognition
import pyttsx3
import subprocess
import webbrowser
from datetime import date, datetime
import time
from chucnang import wikipedia, weather, yearold
import os


shin_ear = speech_recognition.Recognizer()
shin_mouth = pyttsx3.init()
shin_brain = ""

age = yearold()
now = datetime.now()
hour = now.strftime("%H")
if int(hour)>=6 and int(hour)<12:
	shin_brain=("Good Morning sir, Welcome to Shin")	
	print('Shin: '+shin_brain)   
	shin_mouth.say(shin_brain)
	shin_mouth.runAndWait()
elif int(hour)>=12 and int(hour)<18:
	shin_brain=("Good Afternoon sir, Welcome to Shin")
	print('Shin: '+shin_brain)   
	shin_mouth.say(shin_brain)
	shin_mouth.runAndWait()
elif int(hour)>=18 and int(hour)<24:
	shin_brain=("Good Night sir, Welcome to Shin") 	
	print('Shin: '+shin_brain)   
	shin_mouth.say(shin_brain)
	shin_mouth.runAndWait()

today=date.today()
day=today.strftime("%a %B %d, %Y")
while  True:

	with speech_recognition.Microphone() as mic:
		print("Shin: I'm Listening")
		shin_ear.adjust_for_ambient_noise(mic)
		audio = shin_ear.record(mic, duration=4)

	print("Shin:....")

	try:
	   you = shin_ear.recognize_google(audio, language='vi')
	except:
		you = "" 
	print("You: "+you) 


	if you == "":
		shin_brain = "I can't hear you, try again"
	elif "date" in you or "Hôm nay ngày bao nhiêu" in you:
		shin_brain = day
	elif "Open YouTube" in you or "Mở YouTube" in you:
		shin_brain = "Youtube is open"
		print('Shin: '+shin_brain)   
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()	
		webbrowser.open('http://youtube.com',autoraise = True)
		os.system("pause")
	elif "Open Facebook" in you or "Mở Facebook" in you:
		shin_brain = "Facebook is open"
		print('Shin: '+shin_brain)   
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		webbrowser.open('http://facebook.com',autoraise = True)
		os.system("pause")
	elif "Open Google" in you or "Mở Google" in you:
		shin_brain = "Google is open"
		print('Shin: '+shin_brain)   
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		webbrowser.open('http://google.com',autoraise = True)
		os.system('pause')
	elif "time" in you or "Mấy giờ rồi" in you: 
		now = datetime.now()
		shin_brain = now.strftime("%H hours %M minutes %S seconds %p")
	elif "introduce yourself" in you or "tự giới thiệu" in you:
		shin_brain = str(f"my name is shin, i was created on 10/6/2021 in Python programming language till now I {age}")   
	elif "open Chrome" in you or "Mở trình duyệt" in you :
		shin_brain = "browser is open"
		print('Shin: '+shin_brain)   
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
		shin_brain = "What Web you want to open ?"
		print('Shin: '+shin_brain)   
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		with speech_recognition.Microphone() as mic:
			print("Shin: I'm Listening")
			shin_ear.adjust_for_ambient_noise(mic)
			audio = shin_ear.record(mic, duration=4)

		print("Shin:....")

		try:
	  	 you = shin_ear.recognize_google(audio, language='vi')
		except:
			you = "" 
		print("You: "+you)  
		webbrowser.open_new_tab('http://{you}.com')
	elif "weather" in you or "thời tiết" in you:
		shin_brain = "what city you want know?"
		print("Shin: "+shin_brain)
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		with speech_recognition.Microphone() as mic:
			print("Shin: I'm Listening")
			shin_ear.adjust_for_ambient_noise(mic)
			audio = shin_ear.record(mic, duration=4)
		try:
	   		you = shin_ear.recognize_google(audio,language='vi')
		except:
			you = "" 
		print("You: "+you) 
		shin_brain = weather(you)
		if "lỗi" in shin_brain:
			you = input("enter your name city again:")
			shin_brain = weather(you)
			print("Shin:"+shin_brain)
			shin_mouth.say(shin_brain)
			break
	elif "Wikipedia" in you:
		shin_brain = "What you want to know?"
		print('Shin: '+shin_brain)
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		with speech_recognition.Microphone() as mic:
			print("Shin: I'm Listening")
			shin_ear.adjust_for_ambient_noise(mic)
			audio = shin_ear.record(mic, duration=4)
			print("Robot:....")
		try:
	  	 you = shin_ear.recognize_google(audio, language='vi')
		except:
			you = "" 
		print("You: "+you) 
		wikipedia.search(you)
		a=wikipedia.page(you)
		text = a.content
		shin_brain=(text)
		if you == "":
			shin_brain = "I can't hear you, try again"	
	elif "bye" in you or "Turn off" in you :
		shin_brain = "Goodbye sir"
		print('Shin: '+shin_brain)
		shin_mouth.say(shin_brain)
		shin_mouth.runAndWait()
		break
	else:
		robot_brain = "I'm fine thank you and you" 

	print('Shin: '+shin_brain)   
	shin_mouth.say(shin_brain)
	shin_mouth.runAndWait()
	
