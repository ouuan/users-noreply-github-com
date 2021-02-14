import requests
import sys

username = sys.argv[1]

res = requests.get(f'https://api.github.com/users/{username}').json()
print(f'{res["id"]}+{res["login"]}@users.noreply.github.com', end='')
