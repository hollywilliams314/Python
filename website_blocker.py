import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours... ")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            # check each line in the hosts file for a website ref and if
            # it is not a website write it back to the file
            file.seek(0) #start at beginning of file
            for line in content:
                if not any(website in line for website in website_list)
                    file.write(line)
            file.truncate()
        print("Fun time!")
    time.sleep(15)
