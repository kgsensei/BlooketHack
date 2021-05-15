# Original code by: kgsensei, Moded by: DaAwesomeGuy
# Copyright (c) 2021 kgsensei. All rights reserved.
try:
	from colorama import init, Fore, Back, Style
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	from selenium import webdriver
	import time,os,json,sys
except Exception:
	import os
	print("="*32)
	print("Installing required packages...")
	print("="*32)
	os.system("pip3 install selenium")
	os.system("pip3 install selenium-wire")
	os.system("pip3 install colorama")
	os.system("pip3 install webdriver-manager")
finally:
	from colorama import init, Fore, Back, Style
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	import time,os,json,sys
init(autoreset=True)

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

platform=None
if sys.platform=="win32" or sys.platform=="cygwin":
	platform="windows"
else:
	platform="other"

def clear():
	if platform=="windows":
		os.system("cls")
	elif platform=="other":
		os.system("clear")
	else:
		print(color.RED+"Error: Your OS doesn't support Blooket Hack.")
		time.sleep(10)
		os._exit(0)

def checkDouble(lst):
	count={}
	for item in lst:
		if item not in count:
			count[item]=1
		else:
			return True
	return False

clear()

print(color.CYAN+"  ____  _             _        _      _   _            _     "+color.PURPLE+"  ____    ___ \n \
"+color.CYAN+"| __ )| | ___   ___ | | _____| |_   | | | | __ _  ___| | __ "+color.PURPLE+" |___ \  / _ \\ \n \
"+color.CYAN+"|  _ \| |/ _ \ / _ \| |/ / _ \ __|  | |_| |/ _` |/ __| |/ / "+color.PURPLE+"   __) || | | | \n \
"+color.CYAN+"| |_) | | (_) | (_) |   <  __/ |_   |  _  | (_| | (__|   <  "+color.PURPLE+"  / __/ | |_| | \n \
"+color.CYAN+"|____/|_|\___/ \___/|_|\_\___|\__|  |_| |_|\__,_|\___|_|\_\ "+color.PURPLE+" |_____(_)___/\n\n\n")

gamePin=input("Game Pin: ")
gameName=input("Nickname: ")

webdriver_location="chromedriver.exe"
options=webdriver.ChromeOptions()
options.use_chromium=True
options.add_experimental_option('excludeSwitches',['enable-logging'])

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
if sys.platform == "darwin":
	driver = webdriver.Chrome(executable_path='/Users/<PUT USER HERE>/Downloads/BlooketHack-master 4/chromedriver.exe')
else:
	driver=webdriver.Chrome(options=options,executable_path=webdriver_location)
questionList=[]
driver.get('https://www.blooket.com/play')
time.sleep(1)
gamepinenter=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/input')
gamepinenter[0].send_keys(gamePin)
gamepinjoin=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]')
gamepinjoin[0].click()
time.sleep(3)
try:
	nameinenter=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
	nameinenter[0].send_keys(gameName)
	nameinjoin=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div')
	nameinjoin[0].click()
except Exception:
	clear()
	print(color.RED+"\n\n\nError: Invalid Game Pin or Error Joining.\n\n\n")
	driver.close()
	time.sleep(10)
	exit(10)

time.sleep(2)

input(color.PINK+"\n\nPress Enter When Ready To Start Cheat\n\n")
clear()
print(color.YELLOW+"\n\n\nPlease Wait, If you get stuck on this for too long please report it.\n\n\n")

for request in driver.requests:
	if request.response:
		if "https://api.blooket.com/api/games?gameId=" in request.url:
			jsondata=request.response.body
			jsondata=jsondata.decode("utf-8")
			jsondata=json.loads(jsondata)

for question in jsondata['questions']:
	questionList.append(question["question"])

if checkDouble(questionList):
	clear()
	print(color.RED+"\n\n\nError: I will not be able to answer a question with the same text as another question.\n")
	input(color.YELLOW+"Press \'Enter\' to Proceed.")

clear()

while True:
	if driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div'):
		try:
			questionShown=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					clear()
					answer=question["correctAnswers"][0]
					print(color.GREEN+"\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
			questionOne = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div')
			questiontwo = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div')
			questionthree = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div')
			questionfour = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div/div')
			if str(questionOne[0].get_attribute("textContent"))==str(answer):
				questionOne[0].click()
			elif str(questiontwo[0].get_attribute("textContent"))==str(answer):
				questiontwo[0].click()
			elif str(questionthree[0].get_attribute("textContent"))==str(answer):
				questionthree[0].click()
			elif str(questionfour[0].get_attribute("textContent"))==str(answer):
				questionfour[0].click()
			print(color.GREEN+"\n\n\nANSWER: "+answer+"\n\n\n")
		except Exception:
			clear()
			print(color.RED+"\n\n\nSomething Bad Happened. This can happen if your going too fast.\n\n\n")
	
	elif driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div'):
		try:
			questionShown=driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					clear()
					answer=question["correctAnswers"][0]
					print(color.GREEN+"\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
			questionOne = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div')
			questiontwo = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div')
			questionthree = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div')
			questionfour = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div/div')
			if str(questionOne[0].get_attribute("textContent"))==str(answer):
				questionOne[0].click()
			elif str(questiontwo[0].get_attribute("textContent"))==str(answer):
				questiontwo[0].click()
			elif str(questionthree[0].get_attribute("textContent"))==str(answer):
				questionthree[0].click()
			elif str(questionfour[0].get_attribute("textContent"))==str(answer):
				questionfour[0].click()
			print(color.GREEN+"\n\n\nANSWER: "+answer+"\n\n\n")
		except Exception:
			clear()
			print(color.RED+"\n\n\nSomething Bad Happened. This can happen if your going too fast.\n\n\n")

	elif driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div'):
		try:
			questionShown=driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					clear()
					answer=question["correctAnswers"][0]
					print(color.GREEN+"\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
			questionOne = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div')
			questiontwo = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div')
			questionthree = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]/div')
			questionfour = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[4]/div/div')
			if str(questionOne[0].get_attribute("textContent"))==str(answer):
				questionOne[0].click()
			elif str(questiontwo[0].get_attribute("textContent"))==str(answer):
				questiontwo[0].click()
			elif str(questionthree[0].get_attribute("textContent"))==str(answer):
				questionthree[0].click()
			elif str(questionfour[0].get_attribute("textContent"))==str(answer):
				questionfour[0].click()
			print(color.GREEN+"\n\n\nANSWER: "+answer+"\n\n\n")
		except Exception:
			clear()
			print(color.RED+"\n\n\nSomething Bad Happened. This can happen if your going too fast.\n\n\n")

	time.sleep(0.25)
