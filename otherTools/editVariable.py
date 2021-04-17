#Script to edit Blooket scores
#Original Code: kgsensei
import requests,json

gamePin=str(input("Game pin: "))
namself=str(input("Nickname: "))
aic=str(input("Animal [See Options]: "))
while True:
     amount=str(input("Amount: "))
     data={
          'Referer':'https://www.blooket.com/',
          'path':str(gamePin)+'/c/'+str(namself),
          'val':{
               'b':str(aic),
               'g':str(amount)
               }
          }
     dead=str(data)
     r=requests.put('https://www.blooket.com/api/firebase/setval',headers=dead)
     print(r.text)
