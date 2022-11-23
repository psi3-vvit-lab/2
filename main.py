#!/usr/bin/env python3

import requests
from colorama import Fore

city = "Kazan,RU"
with open("appid", "r") as f:
    appid = f.read()

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={"q": city, "units": "metric", "lang": "ru", "APPID": appid})
data = res.json()

print(f"{Fore.LIGHTBLUE_EX}Погода сейчас:")
print(f"{Fore.LIGHTBLACK_EX}Город ...................... {Fore.WHITE}{city}")
print(f"{Fore.LIGHTBLACK_EX}Погодные условия ........... {Fore.WHITE}{data['weather'][0]['description']}")
print(f"{Fore.LIGHTBLACK_EX}Температура ................ {Fore.WHITE}{data['main']['temp']}")
print(f"{Fore.LIGHTBLACK_EX}Минимальная температура .... {Fore.WHITE}{data['main']['temp_min']}")
print(f"{Fore.LIGHTBLACK_EX}Максимальная температура ... {Fore.WHITE}{data['main']['temp_max']}")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()

print(f"\n{Fore.LIGHTBLUE_EX}Прогноз погоды на неделю:")
for i in data['list']:
    print(f"{Fore.YELLOW}{i['dt_txt']}")
    print(f"{Fore.LIGHTBLACK_EX}Температура ........ {Fore.WHITE}{i['main']['temp']:+.0f}")
    print(f"{Fore.LIGHTBLACK_EX}Погодные условия ... {Fore.WHITE}{i['weather'][0]['description']}")
    print(f"{Fore.RESET}")
