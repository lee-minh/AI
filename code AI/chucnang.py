import wikipedia
import requests
import json
from gtts import gTTS
from playsound import playsound
import os
from datetime import time, datetime
yearold = ()
language='vi'
def noi(text):  # Hàm nói
    print("Shin: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("audio.mp3")
    playsound("audio.mp3")
    os.remove("audio.mp3")
def yearold(year_1, day_1, month_1): #hàm tính tuổi
	now = datetime.now()
	year=int(now.strftime("%Y"))
	month = int(now.strftime("%m"))
	day = int(now.strftime("%d"))
	year_old = int(year - year_1 - 2000)
	month_old = int(month - month_1)
	day_old = int(day - month_1)
	if day_old <= 0:
		if int(year%4) == 0:
			if month == 1 or 3 or 5 or 7 or 9 or 11:
				month_old = month_old - 1 
				day_old =31 - day_old
			elif month == 2:
				month_old =month_old - 1
				day_old = 29 - day_old
			elif month == 4 or 6 or 8 or 10 or 12 :
				month_old = month_old -1
				day_old = 30 - day_old
		else:
			if month == 1 or 3 or 5 or 7 or 9 or 11:
				month_old = month_old - 1 
				day_old =31 - day_old
			elif month == 2:
				month_old =month_old - 1
				day_old = 28 - day_old
			elif month == 4 or 6 or 8 or 10 or 12 :
				month_old = month_old -1
				day_old = int(30 - day_old) 
	shin_brain = (f"{day_old} day {month_old} month {year_old} year ")
	return shin_brain
wikipedia.set_lang("en")
def weather(city):  #hàm thời tiết
	response=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=5a7a7bb9e610f268ddc31c0aa02cca34".format(city))
	data = response.text
	jsondata = json.loads(data)
	if jsondata['cod'] != 404:
		y= jsondata['main']
		temp = int(y['temp']) - 273
		pressure = y['pressure']
		humidiy = y['humidity']
		x = jsondata['weather']
		description = x[0]['description']
		shin_brain =str(city) + " hiện đang có " + str(description)+", Nhiệt độ là "+ str(temp)+" độ C, "+" Độ ẩm là "+str(humidiy)+"%"
	else :
		shin_brain = "lỗi"
	return shin_brain

def main():
	pass

if __name__ == "__main__":
	main()