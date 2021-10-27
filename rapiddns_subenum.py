#Usage
#python3.7 rapiddns.py tesla.com|sed 's/,/\n/g'|grep tesla |sed 's/<td>//g'|sed 's\</td>\\g'|grep -v href
#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import sys
domain=sys.argv[1]

url = "https://rapiddns.io:443/subdomain/"+domain+"?full=1&down=1#result"

payload = ""
headers = {
    "Cookie": "_ga=GA1.2.572792676.1635363324; _gid=GA1.2.79979471.1635363324",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Connection": "close",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Dest": "document",
    "Host": "rapiddns.io",
    "Accept-Encoding": "gzip, deflate",
    "Sec-Fetch-Mode": "navigate",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-User": "?1",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua-Mobile": "?0"
}

response = requests.request("GET", url, data=payload, headers=headers)

soup=BeautifulSoup(response.text, "html5lib")
gdp_table = soup.find("tbody")
gdp_table_data = gdp_table.find_all("td")
print(gdp_table_data)
