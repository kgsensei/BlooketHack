# Copyright (c) 2021 kgsensei. All rights reserved.
try:
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	from selenium.common.exceptions import NoSuchElementException
	import time, json, random, sys, os
except Exception:
	import os
	print(("="*32)+"\nInstalling required packages...\n"+("="*32))
	os.system("py -m pip install --upgrade pip")
	os.system("py -m pip install selenium")
	os.system("py -m pip install selenium-wire")
finally:
	from selenium.webdriver.common.keys import Keys
	from seleniumwire import webdriver
	from selenium.common.exceptions import NoSuchElementException
	import time, json, random, sys, os

autoAnswer=False
platform=None
jsondata=None
autoOpen=False
allowReParse=True
questionList=[]

if sys.platform=="win32" or sys.platform=="cygwin":
	platform="windows"
else:platform="other"

# Function to check for double items within list
def checkDouble(lst):
	count={}
	for item in lst:
		if item not in count:count[item]=1
		else:return True
	return False

# Initialize webdriver variables [make stuff work]
options=webdriver.ChromeOptions()
options.use_chromium=True
options.add_argument("--start-maximized")
options.add_argument('--disable-extensions')
options.add_argument("--disable-plugins-discovery")
options.add_argument('--profile-directory=Default')
options.add_experimental_option('excludeSwitches',['enable-logging'])

# Find location that chrome is installed
if os.path.isfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
elif os.path.isfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
elif sys.platform=="darwin":options.binary_location=r'/Applications/Google Chrome.app'
else:
	print("Error: This cheat requires chrome to be installed.")
	time.sleep(10)
	os._exit(0)

# Set path for different operating systems
if sys.platform=="darwin":driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
else:driver=webdriver.Chrome(options=options,executable_path="chromedriver.exe")

# Show new main menu for cheat
driver.execute_script("document.getElementsByTagName('body')[0].innerHTML='<div style=\"color:white; \
	background-color:rgb(25,25,25);width:100%;height:100%;position:absolute;z-index:9999\"><div style= \
	\"position:absolute;left:10%;top:7%;\"><h1>Blooket Hack v5</h1><h3>By: kgsensei</h3><h6>Copyright (c) \
	2021 kgsensei</h6><br><br><h2>Enter the game pin to join:</h2><br><input style=\"outline:none \
	background-color:transparent;border-style:none;width:100%;height:50px;font-size:25px;background-color: \
	rgb(15,15,15);color:white;\" max=\"6\" maxlength=\"6\" id=\"gamePin\" placeholder=\"Game Pin\"><br><br> \
	Do Auto Answer: <input type=\"checkbox\" id=\"DoAutoAnswer\"><br><br><h3> \
	Have fun and be sure to report any issues.</h3></div>'; \
	document.getElementsByTagName('body')[0].style='padding:0px;margin:0px;font-family:\"Segoe UI\", \
	Tahoma,Geneva,Verdana,sans-serif;';params=\"\"; \
	document.addEventListener('keyup',function(e){ \
		if(e.key==='Enter'||e.keyCode===13){ \
			if(document.getElementById('DoAutoAnswer').checked){params=params+\"autoAnswer,\"} \
			fetch(\"https://kgsensei.dev/?params=\"+params).then(data=>{ \
				window.location.href=\"https://www.blooket.com/play?id=\"+document.getElementById(\"gamePin\").value; \
			}) \
		} \
	}); \
	document.title=\"Blooket Hack v5\"")

# Wait for request to load, when it does log answer information
while jsondata==None:
	for request in driver.requests:
		if request.response:
			if "api.blooket.com/api/games?gameId=" in request.url:
				jsondata=request.response.body
				jsondata=jsondata.decode("utf-8",errors="ignore")
				jsondata=json.loads(jsondata)
				break
			if "https://kgsensei.dev/?params=" in request.url and allowReParse==True:
				x=(request.url).replace("https://kgsensei.dev/?params=","").split(",")
				if "autoAnswer" in x:
					autoAnswer=True
				allowReParse=False

# Append questions and answers to the question list variable
for question in jsondata['questions']:
	questionList.append(question["question"])

# Check if element exists
def exists(classname:str):
    try:
        if driver.find_element_by_css_selector(classname):return True
    except(Exception,NoSuchElementException):return False

# Check for double answer
if checkDouble(questionList):
	print("Error: There are multiple questions with the same content, because of the way this cheat works that means it will not be able to answer those questions.\nFor example: The \"Flags of the World\" set, because every question says \"What flag is this?\".")
	input("Press \'Enter\' to run the cheat anyway.")

while True:

	# Every Game Correct Answer and Auto Answer Cheat
	try:
		if exists("#qText"):
			questionShown=driver.find_element_by_css_selector('#qText')
			questionShown=questionShown.get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					print("ANSWER DETECTED: "+str(question["correctAnswers"][0]))
					if exists('#q1'):
						tmpTag=driver.find_element_by_css_selector('#q1')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							if autoAnswer==False:
								driver.execute_script('document.getElementById("q1").innerHTML=document.getElementById("q1").innerHTML+"_[Correct]"')
							else:tmpTag.click()
					if exists('#q2'):
						tmpTag=driver.find_element_by_css_selector('#q2')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							if autoAnswer==False:
								driver.execute_script('document.getElementById("q2").innerHTML=document.getElementById("q2").innerHTML+"_[Correct]"')
							else:tmpTag.click()
					if exists('#q3'):
						tmpTag=driver.find_element_by_css_selector('#q3')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							if autoAnswer==False:
								driver.execute_script('document.getElementById("q3").innerHTML=document.getElementById("q3").innerHTML+"_[Correct]"')
							else:tmpTag.click()
					if exists('#q4'):
						tmpTag=driver.find_element_by_css_selector('#q4')
						if str(tmpTag.get_attribute("textContent"))==str(question["correctAnswers"][0]):
							if autoAnswer==False:
								driver.execute_script('document.getElementById("q4").innerHTML=document.getElementById("q4").innerHTML+"_[Correct]"')
							else:tmpTag.click()
	except Exception as e:
		print("Error: "+str(e))

	# This section of code is for a future feature.

	"""
	# This section is for opening boxes [Gold Only]
	try:
		if autoOpen==True and "/play/gold" in driver.current_url():
			if exists('.styles__choice1___nP-pT-camelCase'):
				x=random.randint(0,2)
				if x==0 and exists('.styles__choice1___nP-pT-camelCase'):
					b=driver.find_element_by_css_selector('.styles__choice1___nP-pT-camelCase')
					b.click()
				elif x==1 and exists('.styles__choice2___nP-pT-camelCase'):
					b=driver.find_element_by_css_selector('.styles__choice2___nP-pT-camelCase').click()
					b.click()
				elif x==2 and exists('.styles__choice3___nP-pT-camelCase'):
					b=driver.find_element_by_css_selector('.styles__choice3___nP-pT-camelCase').click()
					b.click()
	except Exception as e:
		print("Error: "+str(e))
	"""

	# Delay to prevent from overprocessing
	time.sleep(0.125)
