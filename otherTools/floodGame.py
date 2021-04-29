import requests, json

gamePin=str(input("Game pin: "))
botsInt=int(input("Bots: "))
for i in range(0,botsInt):
  requests.put("https://api.blooket.com/api/firebase/join",data={"id":gamePin,"name":"blooketbad"},headers={"Referer":"https://www.blooket.com/"})
  
