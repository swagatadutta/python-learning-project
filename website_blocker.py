import time
from datetime import  datetime as dt

host_temp=r"C:\Users\kishorkumar\PycharmProjects\Python megacourse\website blocker\hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"

redirect="127.0.0.1"
website_list=["www.facebook.com", "www.youtube.com", "www.amazon.in", "www.myntra.com"]

while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, 12)< dt.now()< dt(dt.now().year,dt.now().month, dt.now().day, 22):
        print("Study Time...")
        with open(host_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+"   "+website+"\n")
    else:
        print("Fun Time...")
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)