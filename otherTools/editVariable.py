#Script to edit Blooket scores
#Original Code: kgsensei
import requests,json,time

gamePin=str(input("Game pin: "))
accName=str(input("Account Name: "))
namself=str(input("Nickname: "))
aic=str(input("Animal [See Options]: "))
while True:
     cPlace=str(input("Place: "))
     amount=str(input("Amount: "))
     #----------------------------------------------------------
     #           Request is Unauthorized - Progress
     #----------------------------------------------------------
     r=requests.put(f'https://api.blooket.com/api/users/goldstats',headers={'Referer':'https://www.blooket.com/','name':accName,'place':cPlace,'gold':amount,'nameUsed':namself,'blookUsed':aic})
     print(r.text)
     time.sleep(5)
