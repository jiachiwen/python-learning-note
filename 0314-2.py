#簡單的hhttp request小技術
import requests 
r=requests.get('https://www.google.com')
print(r.text)