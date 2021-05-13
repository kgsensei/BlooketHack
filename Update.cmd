@echo off
title Blooket Hack Updater
timeout /t 5 | echo: && echo: && echo    Installing update of Blooket Hack [Does NOT install ALL the updated files] && echo: && echo:
curl "https://raw.githubusercontent.com/kgsensei/BlooketHack/master/main.py" --output "main.py"
curl "https://raw.githubusercontent.com/kgsensei/BlooketHack/master/chromedriver.exe" --output "chromedriver.exe"
curl "https://raw.githubusercontent.com/kgsensei/BlooketHack/master/README.md" --output "README.md"
curl "https://raw.githubusercontent.com/kgsensei/BlooketHack/master/LICENSE" --output "LICENSE"
curl "https://raw.githubusercontent.com/kgsensei/BlooketHack/master/.gitattributes" --output ".gitattributes"
