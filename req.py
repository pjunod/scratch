import requests
import sys
import string

url = sys.argv[1]

req = requests.get(url)

print(req.json())

num = [1, 2, 4, 3]

foo = "abc"

string.