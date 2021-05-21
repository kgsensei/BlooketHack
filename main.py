# Original code by: kgsensei
# Copyright (c) 2021 kgsensei. All rights reserved.

#Import required libraries
try:
	from colorama import init, Fore, Back, Style
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	import time,os,json,sys
except Exception:
	import os
	print("="*32)
	print("Installing required packages...")
	print("="*32)
	try:
		os.system("pip install selenium")
		os.system("pip install selenium-wire")
		os.system("pip install colorama")
	except Exception:
		os.system("pip3 install selenium")
		os.system("pip3 install selenium-wire")
		os.system("pip3 install colorama")
finally:
	from colorama import init, Fore, Back, Style
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	import time,os,json,sys
init(autoreset=True)

#Setup color classes
class color:
     PURPLE='\033[95m'
     CYAN='\033[96m'
     DARKCYAN='\033[36m'
     BLUE='\033[94m'
     GREEN='\033[92m'
     YELLOW='\033[93m'
     RED='\033[91m'
     BOLD='\033[1m'
     UNDERLINE='\033[4m'
     END='\033[0m'
     PINK='\033[35m'

#Detect platform
platform=None
if sys.platform=="win32" or sys.platform=="cygwin":
	platform="windows"
else:
	platform="other"

#Clear the screen, supports different platforms
def clear():
	if platform=="windows":
		os.system("cls")
	else:
		os.system("clear")

#Function to check for 2 questions with same content
def checkDouble(lst):
	count={}
	for item in lst:
		if item not in count:
			count[item]=1
		else:
			return True
	return False

clear()

#Banner art
print(color.CYAN+"  ____  _             _        _      _   _            _     "+color.PURPLE+"  ____    ___ \n \
"+color.CYAN+"| __ )| | ___   ___ | | _____| |_   | | | | __ _  ___| | __ "+color.PURPLE+" |___ \  / _ \\ \n \
"+color.CYAN+"|  _ \| |/ _ \ / _ \| |/ / _ \ __|  | |_| |/ _` |/ __| |/ / "+color.PURPLE+"   __) || | | | \n \
"+color.CYAN+"| |_) | | (_) | (_) |   <  __/ |_   |  _  | (_| | (__|   <  "+color.PURPLE+"  / __/ | |_| | \n \
"+color.CYAN+"|____/|_|\___/ \___/|_|\_\___|\__|  |_| |_|\__,_|\___|_|\_\ "+color.PURPLE+" |_____(_)___/\n\n\n")

#User information for joining the game
gamePin=input("Game Pin: ")
gameName=input("Nickname: ")

#Start working on selenium webdriver variables
webdriver_location="chromedriver.exe"
options=webdriver.ChromeOptions()
options.use_chromium=True
options.add_experimental_option('excludeSwitches',['enable-logging'])

#Get and set chrome install location [Uses most common locations with file detection]
if os.path.isfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):
	options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
elif os.path.isfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):
	options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
elif sys.platform=="darwin":
	options.binary_location=r'/Applications/Google Chrome.app'
else:
	print(color.RED+"Error: Blooket Hack Requires Chrome To Be Installed.")
	time.sleep(10)
	os._exit(0)

#Sets webdriver variable [Platform dependent]
if sys.platform=="darwin":
	driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
else:
	driver=webdriver.Chrome(options=options,executable_path=webdriver_location)

questionList=[]

#Join game and set up that stuff
driver.get('https://www.blooket.com/play')
time.sleep(1)
try:
	gamepinenter=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/input')
	gamepinenter[0].send_keys(gamePin)
	gamepinjoin=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]')
	gamepinjoin[0].click()
	time.sleep(3)
	nameinenter=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
	nameinenter[0].send_keys(gameName)
	nameinjoin=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div')
	nameinjoin[0].click()
except Exception:
	clear()
	print(color.RED+"\n\n\nError: Unknown Error While Joining.\n\n\n")
	driver.close()
	time.sleep(10)
	exit(10)

time.sleep(2)

#Wait for the user to allow cheat
input(color.PINK+"\n\nPress Enter When Ready To Start Cheat\n\n")
clear()

#Get all requests made while loading the website
for request in driver.requests:
	#If the request has a response contine
	if request.response:
		#If the url contains "https://api.blooket.com/api/games?gameId=" contine. This url has game data including answers and questions
		if "https://api.blooket.com/api/games?gameId=" in request.url:
			jsondata=request.response.body
			jsondata=jsondata.decode("utf-8")
			jsondata=json.loads(jsondata)

#Make a questions list
for question in jsondata['questions']:
	questionList.append(question["question"])

#Check for double questions
if checkDouble(questionList):
	clear()
	print(color.RED+"\n\n\nError: Multiple questions with same content detected. I will not be able to answer these questions.")
	input(color.YELLOW+"Press \'Enter\' to Proceed.")

#Main cheat function
clear()
while True:
	#Detect if question exists
	if driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div'):
		try:
			#Try to match the question with the correct answer
			questionShown=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					clear()
					#Print correct answer
					print(color.GREEN+"\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
		except Exception:
			clear()
			print(color.RED+"\n\n\nSomething Bad Happened. This can happen if your going too fast.\n\n\n")

	#Detect if question exists
	elif driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div'):
		try:
			#Try to match the question with the correct answer
			questionShown=driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					clear()
					#Print correct answer
					print(color.GREEN+"\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
		except Exception:
			clear()
			print(color.RED+"\n\n\nSomething Bad Happened. This can happen if your going too fast.\n\n\n")

	#Detect if question exists
	elif driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div'):
		try:
			#Try to match the question with the correct answer
			questionShown=driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					clear()
					#Print correct answer
					print(color.GREEN+"\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
		except Exception:
			clear()
			print(color.RED+"\n\n\nSomething Bad Happened. This can happen if your going too fast.\n\n\n")

	#Wait so system doesn't overload. Can modify btw.
	time.sleep(0.25)
	
