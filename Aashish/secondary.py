import requests
import sys
import subprocess

url = sys.argv[1]
flag_status = sys.argv[2]

#print("import successfull")
#print(url, flag_status)

def saveContent(url):

    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    #only getting 200 characters to ensure we get source of the page.
    print(r.content[:200])

    #extract the contents and save to file
    f = open('myfile.txt','w')
    extracts = str(r.content)

    f.write(extracts)
    f.close()

def checkFlag(flag_status):
    if flag_status == "set":
        subprocess.call(["python","-m","http.server"])     
    print("Http_server is not being used.")

saveContent(url)
checkFlag(flag_status)
