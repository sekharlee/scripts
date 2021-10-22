#python3.7 reverse_lookup.py Red+Bull+GmbH |sed 's/,/\n/g'|grep -vE '(^|[^0-9])[0-9]{4}-[0-9]{2}-[0-9]{2}($|[^0-9])'|sed 's/<td>//g'|cut -d/ -f1|egrep -v '\.<|<td w|Registrar<|Domain| MARKMONITOR'|sed 's/<//g'|egrep -v  '\. '|grep '\.'|awk NF

#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import sys
org=sys.argv[1]
url = "https://viewdns.info:443/reversewhois/?q="+org

payload = ""
headers = {
    "Cookie": "PHPSESSID=f7td64rn96trh4edd8cn8eulg2; __utma=126298514.1798190869.1634858614.1634858614.1634858614.1; __utmc=126298514; __utmz=126298514.1634858614.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _fbp=fb.1.1634858621407.566301945; __gads=ID=ab67c3e3e09d36ca-22e3294fcbcc00cb:T=1634858616:RT=1634858616:S=ALNI_MYOZ72SkAidkWBixqydIW9OBnYHiw; __utmb=126298514.7.10.1634858614",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Connection": "close",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Dest": "document",
    "Host": "viewdns.info",
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
gdp_table = soup.find("table", attrs={"border": "1"})
gdp_table_data = gdp_table.find_all("td")
print(gdp_table_data)
