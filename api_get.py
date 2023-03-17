import requests as re

# http get, post, put, delete
# pip install requests

# http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/

response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/CHF/")
print(response)
# 200 ok
# 4.. bledy
# 5.. bledy serwera
table = response.json()
print(table)
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])