#Script to kick player from Blooket
#Original Code: iCrazeiOS; Modifyed By: kgsensei
import requests

gamePin=str(input("Game pin: "))
name=str(input("Name to kick: "))
r=requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={name}",headers={"Referer":"https://www.blooket.com/"})
print(r.text)
