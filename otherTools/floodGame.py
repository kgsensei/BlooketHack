# Original code by kgsensei
# Code modified by Copycat#8110

try:
    import requests,json
except Exception:
    import os
    print("Installing required package (request)")
    os.system("pip install requests")
    import requests,json

while True:
    gameID=str(input("Game ID: "))
    if len(gameID) == 6:
        break
    else:
        print("\nThe Game ID should be 6 numbers")
        
botsName = str(input("Bot name: "))

while True:
    tempBots=input("Bots: ")
    try:
        botsInt = int(tempBots)
    except ValueError:
        print("\nPlease input a number")
    else:
        break

if botsInt > 60:
    botsInt = 60
    print("\nBots changed to 60")
    print("You can only have a maximum of 60 players in a Blooket game.")

for i in range(0,botsInt):
    r = requests.put("https://api.blooket.com/api/firebase/join", data={"id":gameID,"name":botsName+' '+str(i)},headers={"Referer":"https://www.blooket.com/"})
    if r.text == """{"success":false,"msg":"taken"}""":
        print("\nName Taken! Choose a different name!")
    if r.text == """{"success":false,"msg":"no game"}""":
        if i > 0:
            print("\nGame Full! " + i + "bots added.")
            break
        print("\nNo game found!")
        break

input("Press Enter to exit ")
