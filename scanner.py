from urllib.request import Request, urlopen
from urllib.parse import urlencode
from twilio.rest import Client
from course import Course
from listofcourses import courses
import random
import re
import time
import sys

def myexcepthook(exc_type, value, tb):
    client.messages.create(from_=sender, body=exc_type.__name__, to="+17788884916")



def wait():
  randDelay = 15 + int(random.randrange(11))
  time.sleep(randDelay) 
  print("done waiting")

# Check seats in the course
def checkSeats(url):
    # Setup request with User-agent and Referer headers
    req = Request(url)
    req.add_header('User-agent', 'Mozilla/5.0')
    # req.add_header('Referer', 'https://www.google.com/')

    # Make request and decode 
    try: 
        res = urlopen(req)
    except Exception as error:
        client.messages.create(from_=sender, body=error, to="+17788884916")
        return "0"
    page = res.read().decode("utf-8")

    # Search html page for seat information
    g = re.search(generalSeats, page)
    return g.group(1)
    
def notify(course):
    message = client.messages.create(
        from_='+16185472934',
        body=course.dept+' '+course.code+' '+course.url,
        to='+17788884916'
    )


    


# courses = []

# while True:

#     dept = input("enter course department: ")
#     code = input("enter course code: ")
#     section = input("enter course section: ")
#     session = input("session W or S: ")
#     year = input("enter year: ")
#     courses.append(Course(dept, code, section, session, year))
#     cont = input("would you like to add another course [y or n]: ")
#     if cont=="n":
#         break
sys.excepthook = myexcepthook
account_sid = "AC832679e2f2245a821e95e6cecde6d2b7"
auth_token = "523e92cca4147462f1a1f9368ffb647a"
client = Client(account_sid, auth_token)
sender = "+16185472934"
client.messages.create(from_=sender, body="up and running", to="+17788884916")
# totalSeats = re.compile("<td width=&#39;200px&#39;>Total Seats Remaining:</td>" + "<td align=&#39;left&#39;><strong>(.*?)</strong></td>")
generalSeats = re.compile("<td width=&#39;200px&#39;>General Seats Remaining:</td>" + "<td align=&#39;left&#39;><strong>(.*?)</strong></td>")
# restrictedSeats = re.compile("<td width=&#39;200px&#39;>Restricted Seats Remaining\*:</td>" + "<td align=&#39;left&#39;><strong>(.*?)</strong></td>")
newlist = []
c=0
while True:
    if len(courses)==0:
        break
    for course in courses:
        seats = checkSeats(course.url)
        print(seats)
        if seats!="0":
            notify(course)
            print("text!")
        else:
            newlist.append(course)
        wait()
        c+=1
        if (c==10):
            client.messages.create(from_=sender, body="still going", to="+17788884916")
    courses = newlist
    newlist = []
    random.shuffle(courses)



