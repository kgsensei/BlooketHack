# Copyright (c) 2021 kgsensei. All rights reserved.

try:
  import requests
except Exception:
  import os
  os.system("pip install requests")
  import requests

gamePin=str(input("Game pin: "))
name=str(input("Name to kick: "))
r=requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={name}",headers={"Referer":"https://www.blooket.com/"})
print(r.text)
