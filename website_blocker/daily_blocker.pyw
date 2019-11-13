import time
from datetime import datetime as dt
hosts_path=r"D:\Work\learning_and_developement\mega_course\website_blocker\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.googlemail.com","gmail.com"]

weekends = ["Sat", "Sun"]
now = dt.now()
work_start = dt(now.year, now.month, now.day, 8)
work_end = dt(now.year, now.month, now.day, 18)

while True:
    now = dt.now()
    day =  now.strftime("%a")
    if work_start < now < work_end and day not in weekends:
        with open("hosts.txt", "r+") as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write("\n" +redirect+ "    "+ website)
        print("Weekdays: Working Hours....")
    else:
        with open("hosts.txt", "r+") as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
                f.truncate()
        print("Fun hours.....")
    time.sleep(5)
   

   