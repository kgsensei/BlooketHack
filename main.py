# Copyright (c) 2021 kgsensei. All rights reserved.
try:
 from colorama import init, Fore, Back, Style
 from selenium.webdriver.common.keys import Keys
 from seleniumwire import webdriver
 import time
 import os
 import json
 import sys
except Exception:
 import os
 print(("="*32)+"\nInstalling required packages...\n"+("="*32))
 os.system("pip install selenium")
 os.system("pip install colorama")
 os.system("pip install selenium-wire")
finally:
 from colorama import init, Fore, Back, Style
 from selenium.webdriver.common.keys import Keys
 from seleniumwire import webdriver
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
#forceWin=input(color.CYAN+"Force Win [Experimental][Y/N]: ")
#abuseTokens=input(color.CYAN+"Add 500 Tokens [Experimental][Y/N]: ")
print(color.CYAN+"Force Win [Patched]\nAdd 500 Tokens [Patched]")
forceWin="n";abuseTokens="n";
webdriver_location="chromedriver.exe"
options=webdriver.ChromeOptions()
options.use_chromium=True
options.add_experimental_option('excludeSwitches',['enable-logging'])
if os.path.isfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe'):options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
elif os.path.isfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
elif sys.platform=="darwin":options.binary_location=r'/Applications/Google Chrome.app'
else:
 print(color.RED+"Error: Blooket Hack Requires Chrome To Be Installed.")
 time.sleep(10)
 os._exit(0)
if sys.platform=="darwin":driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
else:driver=webdriver.Chrome(options=options,executable_path=webdriver_location)
questionList=[]
base=100
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
 print(color.RED+"\n\nError: Unknown Error While Joining.\n\n")
 driver.close()
 time.sleep(10)
 exit(10)
time.sleep(2)
input(color.CYAN+"\n\nPress Enter When Ready To Start Cheat\n\n")
for request in driver.requests:
 if request.response:
  if "https://api.blooket.com/api/games?gameId=" in request.url:
   jsondata=request.response.body
   jsondata=jsondata.decode("utf-8")
   jsondata=json.loads(jsondata)
for question in jsondata['questions']:questionList.append(question["question"])
if checkDouble(questionList):
 print(color.RED+"Error: Multiple questions with same content detected. I will not be able to answer these questions.")
 input(color.YELLOW+"Press \'Enter\' to Proceed.")
def interceptor(request):
 global base
 if "https://api.blooket.com/api/firebase/setval" in request.url and forceWin.lower()=="y":
  body=request.body.decode('utf-8')
  data=json.loads(body)
  data['val']['g']=base
  data['val']['d']=base
  data['val']['ca']=base
  data['val']['pr']=base
  data['val']['t']=0
  base=base+base
  request.body=json.dumps(data).encode('utf-8')
  del request.headers['Content-Length']
  request.headers['Content-Length']=str(len(request.body))
 if "https://api.blooket.com/api/users/addtokens" in request.url and abuseTokens.lower()=="y":
  body=request.body.decode('utf-8')
  data=json.loads(body)
  print(data['addedTokens'])
  data['addedTokens']=500
  request.body=json.dumps(data).encode('utf-8')
  del request.headers['Content-Length']
  request.headers['Content-Length']=str(len(request.body))
driver.request_interceptor=interceptor
clear()
while True:
 if driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div'):
  try:
   questionShown=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div')
   questionShown=questionShown[0].get_attribute("textContent")
   for question in jsondata['questions']:
    if str(question["question"])==questionShown:
     clear()
     print(color.CYAN+"\n\nANSWER: "+str(question["correctAnswers"][0]))
  except Exception:
   clear()
   print(color.RED+"\n\nError: Unable to detect question content.")
 elif driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div'):
  try:
   questionShown=driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div')
   questionShown=questionShown[0].get_attribute("textContent")
   for question in jsondata['questions']:
    if str(question["question"])==questionShown:
     clear()
     print(color.CYAN+"\n\nANSWER: "+str(question["correctAnswers"][0]))
  except Exception:
   clear()
   print(color.RED+"\n\nError: Unable to detect question content.")
 elif driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div'):
  try:
   questionShown=driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div')
   questionShown=questionShown[0].get_attribute("textContent")
   for question in jsondata['questions']:
    if str(question["question"])==questionShown:
     clear()
     print(color.CYAN+"\n\nANSWER: "+str(question["correctAnswers"][0]))
  except Exception:
   clear()
   print(color.RED+"\n\nError: Unable to detect question content.")
 time.sleep(0.25)
