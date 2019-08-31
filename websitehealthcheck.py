import requests,os,time

SITE_URL=""
time.sleep(60)
while True:
    response=requests.get(SITE_URL)
    print(response)
    if response.status_code!=200:
          print ("'+SITE_URL+' is down")
