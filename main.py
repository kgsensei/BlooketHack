# Copyright (c) 2021 kgsensei. All rights reserved.
try:
	from colorama import init, Fore, Back, Style
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	from selenium.common.exceptions import NoSuchElementException
	import time
	import os
	import json
	import sys
except Exception:
	import os
	print(("="*32)+"\nInstalling required packages...\n"+("="*32))
	os.system("py -m pip install --upgrade pip")
	os.system("py -m pip install selenium")
	os.system("py -m pip install \"colorama==0.4.3\"")
	os.system("py -m pip install selenium-wire")
finally:
	from colorama import init, Fore, Back, Style
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	from selenium.common.exceptions import NoSuchElementException
	import time
	import os
	import json
	import sys

init(autoreset=True)

class color:
	PURPLE='\033[95m'
	CYAN='\033[96m'
	BLUE='\033[94m'
	GREEN='\033[92m'
	YELLOW='\033[93m'
	RED='\033[91m'
	BOLD='\033[1m'
	END='\033[0m'

platform=None
if sys.platform=="win32" or sys.platform=="cygwin":platform="windows"
else:platform="other"

def clear():
	if platform=="windows":os.system("cls")
	else:os.system("clear")

def checkDouble(lst):
	count={}
	for item in lst:
		if item not in count:count[item]=1
		else:return True
	return False

clear()

print(color.CYAN+"  ____  _             _        _      _   _            _     "+color.PURPLE+"        _____\n \
"+color.CYAN+"| __ )| | ___   ___ | | _____| |_   | | | | __ _  ___| | __ "+color.PURPLE+" __   _|___ /\n \
"+color.CYAN+"|  _ \| |/ _ \ / _ \| |/ / _ \ __|  | |_| |/ _` |/ __| |/ / "+color.PURPLE+" \ \ / / |_ \\\n \
"+color.CYAN+"| |_) | | (_) | (_) |   <  __/ |_   |  _  | (_| | (__|   <  "+color.PURPLE+"  \ V / ___) |\n \
"+color.CYAN+"|____/|_|\___/ \___/|_|\_\___|\__|  |_| |_|\__,_|\___|_|\_\ "+color.PURPLE+"   \_/ |____/\n\n\n")
gamePin=input(color.CYAN+"Game Pin: ")
gameName=input(color.CYAN+"Nickname: ")

webdriver_location="chromedriver.exe"
options=webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.use_chromium=True
options.add_experimental_option('excludeSwitches',['enable-logging'])
if os.path.isfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
elif os.path.isfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
elif sys.platform=="darwin":options.binary_location=r'/Applications/Google Chrome.app'
else:
	print(color.RED+"Error: This cheat requires chrome to be installed.")
	time.sleep(10)
	os._exit(0)

if sys.platform=="darwin":driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
else:driver=webdriver.Chrome(options=options,executable_path=webdriver_location)
questionList=[]
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
	print(color.RED+"Error: Unknown Error While Joining.")
	driver.close()
	time.sleep(10)
	exit(10)

print(color.CYAN+"Cheat will start soon...")
#https://api.blooket.com/api/games?gameId=609d3aebe76402001b2c0ab9
request=driver.wait_for_request('://api.blooket.com/api/games?gameId=',timeout=600)
jsondata=request.response.body
jsondata=jsondata.decode("utf-8")
jsondata=json.loads(jsondata)
for question in jsondata['questions']:
	questionList.append(question["question"])

def exists(classname:str):
	try:
		if driver.find_element_by_css_selector(classname):
			return True
	except(Exception,NoSuchElementException):
		return False

if checkDouble(questionList):
	print(color.RED+"Error: There are multiple questions with the same content, because of the way this cheat works that means it will not be able to answer those questions.\nFor example: The \"Flags of the World\" set, because every question says \"What flag is this?\".")
	input(color.RED+"Press \'Enter\' to run the cheat anyway.")

while True:
	if exists("#qText"):
		try:
			questionShown=driver.find_element_by_css_selector('#qText')
			questionShown=questionShown.get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					print(color.CYAN+"ANSWER DETECTED: "+str(question["correctAnswers"][0]))
					if exists('#q1'):
						tmpTag=driver.find_element_by_css_selector('#q1')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							driver.execute_script('document.getElementById("q1").innerHTML=document.getElementById("q1").innerHTML+" [Correct]"')
					if exists('#q2'):
						tmpTag=driver.find_element_by_css_selector('#q2')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							driver.execute_script('document.getElementById("q2").innerHTML=document.getElementById("q2").innerHTML+" [Correct]"')
					if exists('#q3'):
						tmpTag=driver.find_element_by_css_selector('#q3')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							driver.execute_script('document.getElementById("q3").innerHTML=document.getElementById("q3").innerHTML+" [Correct]"')
					if exists('#q4'):
						tmpTag=driver.find_element_by_css_selector('#q4')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							driver.execute_script('document.getElementById("q4").innerHTML=document.getElementById("q4").innerHTML+" [Correct]"')
		except Exception:print(color.RED+"An internal error occured...")
	time.sleep(0.2)
