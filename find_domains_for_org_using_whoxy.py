#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import sys
#usage
#python3.7 whoxy.py https://www.whoxy.com/keyword/tesla  |grep  '\.\./'|egrep -iv 'domains|domain|#|\.php|whois'|sed 's\../\\g'
echo "Usage "
echo "python3.7 whoxy.py https://www.whoxy.com/keyword/tesla  |grep  '\.\./'|egrep -iv 'domains|domain|#|\.php|whois'|sed 's\../\\g'"
url =  sys.argv[1]

payload = ""
headers = {
    "Cookie": "PHPSESSID=cb4ca3599dc48d531d99e073e151d9d2; source_domain=www.google.com; source_webpage=https%3A%2F%2Fwww.google.com%2F; site_entry_time=2021-10-21+22%3A20%3A32; _ga=GA1.2.739457975.1634854836; _gid=GA1.2.1718956466.1634854836; __gads=ID=a1a81878f49d3cf8-2246dcb8c5cc0098:T=1634854836:RT=1634854836:S=ALNI_MYSytwi8lXwAj9yVbYcGeSOHePjWA; _gat=1PHPSESSID=cb4ca3599dc48d531d99e073e151d9d2; source_domain=www.google.com; source_webpage=https%3A%2F%2Fwww.google.com%2F; site_entry_time=2021-10-21+22%3A20%3A32; _ga=GA1.2.739457975.1634854836; _gid=GA1.2.1718956466.1634854836; __gads=ID=a1a81878f49d3cf8-2246dcb8c5cc0098:T=1634854836:RT=1634854836:S=ALNI_MYSytwi8lXwAj9yVbYcGeSOHePjWA; _gat=1",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Dest": "document",
    "Host": "www.whoxy.com",
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
for link in soup.find_all('a'):
    print(link.get('href'))
