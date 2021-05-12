#Script to edit Blooket scores
#Original Code: kgsensei

import time
print("\nHey, kgsensei here, This was broken a while ago and I don't plan on fixing it.\n\nSorry about that.\n\nThe files source code is after this line.")
time.sleep(10)
exit()

#The original code is here: [Again, Sorry it broke.]
import requests,json,time
gamePin=str(input("Game pin: "))
accName=str(input("Account Name: "))
namself=str(input("Nickname: "))
aic=str(input("Animal [See Options]: "))
while True:
     amount=str(input("Amount: "))
     r=requests.put(f'https://api.blooket.com/api/users/goldstats',headers={'Referer':'https://www.blooket.com/','name':accName,'gold':amount,'nameUsed':namself,'blookUsed':aic})
     print(r.text)
     time.sleep(1)
