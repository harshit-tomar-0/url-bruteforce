#wordlist dns enumeration
from requests import get
from random import choice,randint
import time,threading
url=input("Enter the url >")
wordlist=input("enter wordlist path>")
numofthread=int(input("enter number of threads >"))
headers_list = [
    {
        "name": "Chrome Windows",
        "headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        }
    },
    {
        "name": "Firefox Windows",
        "headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) "
                "Gecko/20100101 Firefox/125.0"
            )
        }
    },
    {
        "name": "Edge Windows",
        "headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
            )
        }
    },
    {
        "name": "Chrome Android",
        "headers": {
            "User-Agent": (
                "Mozilla/5.0 (Linux; Android 13; Pixel 7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Mobile Safari/537.36"
            )
        }
    },
    {
        "name": "Firefox Android",
        "headers": {
            "User-Agent": (
                "Mozilla/5.0 (Android 13; Mobile; rv:125.0) "
                "Gecko/125.0 Firefox/125.0"
            )
        }
    },
    {
        "name": "Samsung Internet",
        "headers": {
            "User-Agent": (
                "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G991B) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "SamsungBrowser/23.0 Chrome/124.0.0.0 Mobile Safari/537.36"
            )
        }
    }
]
def url_scannner(pyld):
    status=get(url+pyld,headers=choice(headers_list)["headers"]).status_code
    if status==200:
        print(url+"/"+pyld+" --> 200")
'''
    else:
        print(url+"/"+pyld+"-->"+str(status))
'''

with open(wordlist) as word:
    payload=word.readlines()
payload=[p for pa in payload for p in pa.split("\n") if p != ""]
threads=[]

for i in range(0,len(payload)+1,numofthread):
    for j in range(i,i+numofthread+1):
        try:
            t=threading.Thread(target=url_scannner,args=(payload[j],))
            t.start()
            threads.append(t)
        except:
            ...
    sleep_time=randint(5,10)
    print("sleeping for ",sleep_time)
    time.sleep(sleep_time)

for thread in threads:
    thread.join()

