For any questions, please join the [discord server](https://discord.com/invite/3r6mkjv6AP) or contact [rdWei](https://www.instagram.com/rdWe_i/).

_I'll only respond to those proposals that are a good match for my schedule and interests, thank you._

---

<div align="center">
  <pre style="display: inline-block; border: 1px solid; padding: 10px;">
 ________  ___ _   _ 
/  ___|  \/  || | | |
\ `--.| .  . || |_| |
 `--. \ |\/| ||  _  |
/\__/ / |  | || | | |
\____/\_|  |_/\_| |_/
   
Social Media Hacking Toolkit
  </pre>
</div>

 

 <h6><p align="center">
    perform different types of <a href="https://github.com/rdWei/SocialMediaHackingToolkit/blob/main/cmd/supported-attack.txt">attacks</a> on many <a href="https://github.com/rdWei/SocialMediaHackingToolkit/blob/main/cmd/supported-social.txt">social media</a>
</p></h6>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/release-v0.3.3-141449" alt=""/>
  <img src="https://img.shields.io/badge/written in-python | php-141449" alt=""/>
  <img src="https://img.shields.io/badge/author-rdWei-141449" alt=""/>
 <h6><p align="center" style="color:yellow">
    <i>please read at least the section regarding <a href="https://github.com/rdWei/SocialMediaHackingToolkit#Trustability">trustability</a>
</i></a>
</p></h6>

---

<h3><p align="center">Disclaimer</p></h3>

The <b>SocialMediaHackingToolkit</b> on GitHub is for <i>educational purposes</i> only. I take no responsibility for its usage by third parties, and any <i>illegal activities</i> are strictly prohibited. Users must <i>comply</i> with security and privacy policies of social media platforms and obtain proper <i>authorization</i>. The toolkit may contain potentially <i>harmful materials</i>. Use at your own <i>risk</i>, adhering to relevant <i>laws and regulations</i>.


<div align="center">

|  tested on   | Yes | No |
|-------|:-----------:|:-----------:|
| Ubuntu      |   X      |           |
| Arch        |     X      |           |
| Void        |       X    |           |           
| Debian      |     X      |           |          
| Kali        |     X      |           |          
| Windows 7   |           |    X       |          
| Windows 11 |     X      |           |          
| Termux |     X      |           |          

</div>


<h3><p align="center">Installation</p></h3>

 <h6><p align="center">
this section explains how to install and run the tool on:<br> ubuntu, arch, void, kali, windows 10+
</p></h6>

---

>first of all if you are on linux create an account [here](https://windscribe.net/login)

<h5><p align="center">Ubuntu / Debian</p></h3>

```
git clone https://github.com/rdWei/SocialMediaHackingToolkit

cd SocialMediaHackingToolkit

cd dependencies

sudo dpkg -i windscribe-cli.deb

windscirbe login 

cd ../cmd

pip3 install -r requirements.txt

cd ..

chmod +x linux.sh

./linux.sh
```

<h5><p align="center">Arch</p></h3>


```
git clone https://github.com/rdWei/SocialMediaHackingToolkit

cd SocialMediaHackingToolkit

yay install windscribe-v2-bin

systemctl start windscribe-cli

windscribe login

cd ../cmd

pip3 install -r requirements.txt

cd ..

chmod +x linux.sh

./linux.sh
```

<h5><p align="center">Void</p></h3>


```
git clone https://github.com/rdWei/SocialMediaHackingToolkit

cd SocialMediaHackingToolkit

cd dependencies

sudo dpkg -i windscribe-cli

xbps-rindex -a windscribe-cli.xbps

windscirbe login 

cd ../cmd

pip3 install -r requirements.txt && cd..

chmod +x linux.sh

./linux.sh
```

<h5><p align="center">Kali Linux</p></h3>


```
git clone https://github.com/rdWei/SocialMediaHackingToolkit

cd SocialMediaHackingToolkit

cd dependencies

sudo dpkg -i windscribe-cli.deb

windscirbe login 

cd ../cmd

pip3 install -r requirements.txt

cd ..

chmod +x linux.sh

./linux.sh
```

<h5><p align="center">Termux</p></h3>


```
git clone https://github.com/rdWei/SocialMediaHackingToolkit

cd SocialMediaHackingToolkit

cd cmd

pip3 install -r requirements.txt

cd ..

chmod +x linux.sh

./linux.sh
```

<h5><p align="center">Windows</p></h3>


```
# download zip file of the repository

# extract zip file and open terminal into "SocialMediaHacking" folder

cd cmd

pip install -r requirements.txt

cd ..

start windows.bat
```


<br>

<h3><p align="center">Technical Description</p></h3>

 <h6><p align="center">
this section explains how the different functionalities of the program work and provides an analysis of their operations.
</p></h6>


---

<h5><p align="center">Mass report</p></h3>

To achieve the mass reporting functionality, the program utilizes the report_headers dictionary. These headers are essential for making **HTTP requests** and providing necessary information to the server. Here is the used headers:

```
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
```

These headers are included in the **HTTP request** to ensure proper communication and provide necessary details to the Instagram Help Center API.

The program's code interacts with the Instagram Help Center's contact form API by sending a **POST request** to the specified URL.

<h5><p align="center">Brute force</p></h3>

The insta_bruteforce function performs a brute force attack on an Instagram account using a provided username and a wordlist of passwords. Here's an overview of how it works:

1. The function takes three parameters: username (target Instagram account), wordlist (filename of the password wordlist), and vpn (VPN usage flag).
2. It reads the wordlist file and stores the passwords in memory.
3. For each password in the wordlist, the function performs the following steps:
	
	- Sends a POST request to the Instagram login API with the provided username and password.
	- If the response indicates a successful login, it displays the password and terminates the program.
	- If the login attempt fails, it moves on to the next password.

4.  If an exception occurs during the process (e.g., network error), it moves on to the next password.
5.  If the VPN flag is set to True, it attempts to change the IP address.


<h5><p align="center">2nd method, currently in use</p></h3>

```
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
```

This function checks if the password is exact, if verification is requested then the password is exact but the user uses two-factor verification, on the other hand if verification is not requested the password is exact

---

<h3><p align="center">Errors</p></h3>

 <h6><p align="center">
this section discusses common errors that can occur in the program and explores their underlying causes.
</p></h6>

- Error 0x00: Letter Instead of Numeric Value

	This error occurs when a letter is 	mistakenly inserted instead of a required numerical value. It commonly happens due to user input or data processing issues where a non-numeric character is provided instead of a valid numeric value.

- Error 0x01: Number Out of Range

	Error 0x01 is triggered when a number outside the expected range is entered within a specific determinant or range. This error is usually caused by user input or a miscalculation resulting in a value that exceeds the allowed range.

- Error 0x02: Incorrect Number in Determinant or Range

	The occurrence of error 0x02 indicates that a number outside the designated determinant or range has been entered. This error typically occurs when a number is provided that falls outside the expected boundaries, and it can be caused by user input or an error in calculations.

- Error 0x03: VPN Usage on Windows

	Error 0x03 is encountered when attempting to use a VPN on a Windows system. This error suggests compatibility issues or incorrect configuration while trying to establish a VPN connection on the Windows operating system.

---
<h3><p align="center">Trustability</p></h3>


you can verify that the program works by testing it on **your profile**, open the wordlist and put **your profile password** in the first place, then start the program and enter your instagram profile nuckname and you will see that the password will come out as correct.


</p></h3>

<div align="center">

| active features | Bruteforce | Mass report | Phishing |
|-------|:-----------:|:-----------:|:-----------:|
| Instagram|   X      |      X     |           |
| Facebook|     X      |           |           |
| Gmail|       X    |           |           |
| Twitter|     X      |   X        |           |

</div> 

<br>

---



<br>

<h3><p align="center">Issues and Suggestions</p></h3>

<p align="center">
  <img src="images/issues.gif" alt=""/>
</p>

If you have encountered an issue with SocialMediaHackingToolkit or would like to suggest an improvement, please report it in our [Issues section](https://github.com/rdWei/SocialMediaHackingToolkit/issues).<br> Please provide as much detail as possible about the issue or suggestion so that we can resolve or implement it as soon as possible.<br> <b>Thank you for your contribution!</b>

<br>



## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=rdWei/socialmediahackingtoolkit&type=Date)](https://star-history.com/#rdWei/socialmediahackingtoolkit&Date)

