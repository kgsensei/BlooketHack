from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
import time, os, json

gamePin=input("Game Pin: ")
gameName=input("Game Name: ")
webdriver_location="chromedriver.exe"
options=webdriver.ChromeOptions()
options.use_chromium=True
options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver=webdriver.Chrome(options=options,executable_path=webdriver_location)
time.sleep(0.5)
driver.get('https://www.blooket.com/play')
time.sleep(1)
gamepinenter=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/input')
gamepinenter[0].send_keys(gamePin)
gamepinjoin=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]')
gamepinjoin[0].click()
time.sleep(4)
nameinenter=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
nameinenter[0].send_keys(gameName)
nameinjoin=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/div')
nameinjoin[0].click()
time.sleep(4)
input("\n\nPress Enter When Ready To Start Cheat\n\n")
for request in driver.requests:
	if request.response:
		if "https://api.blooket.com/api/games?gameId=" in request.url:
			jsondata=request.response.body
			jsondata=jsondata.decode("utf-8")
			jsondata=json.loads(jsondata)
while True:
	if driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div'):
		try:
			questionShown=driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					os.system("cls")
					print("\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
		except Exception:
			os.system("cls")
			print("\n\n\nSomething Bad Happened... This can happen if your going too fast.\n\n\n")
	elif driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div'):
		try:
			questionShown=driver.find_elements_by_xpath('//*[@id="left"]/div/div[1]/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					os.system("cls")
					print("\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
		except Exception:
			os.system("cls")
			print("\n\n\nSomething Bad Happened... This can happen if your going too fast.\n\n\n")
	elif driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div'):
		try:
			questionShown=driver.find_elements_by_xpath('//*[@id="body"]/div[3]/div/div[1]/div')
			questionShown=questionShown[0].get_attribute("textContent")
			for question in jsondata['questions']:
				if str(question["question"])==questionShown:
					os.system("cls")
					print("\n\n\nANSWER: "+str(question["correctAnswers"][0])+"\n\n\n")
		except Exception:
			os.system("cls")
			print("\n\n\nSomething Bad Happened... This can happen if your going too fast.\n\n\n")
	time.sleep(0.25)
