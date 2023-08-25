import requests
from platform import uname as name
import random, os
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
print (f"""{lrd}
####   ##### ####    ###   ####   ###### ##### ####
## ##  ##    ## ##  ## ##  ## ##    ##   ##    ## ##
## ##  ##    ## ## ##   ## ## ##    ##   ##    ## ##
####   ####  ####  ##   ## ####     ##   ####  ####
## ##  ##    ##    ##   ## ## ##    ##   ##    ## ##
## ##  ##    ##     ## ##  ## ##    ##   ##    ## ##
##  ## ##### ##      ###   ##  ##   ##   ##### ##  ##
       
     {lrd}  github : {lgn}github.com/esfelurm
       
     {lrd}  channel Telegram :{lgn} @esfelurm
     
""")
target = input(f"{lrd}[{yw}URL{lrd}] {lgn}Enter Username target :{pe} ")
method = input(f"""

    {lrd}[{yw}1{lrd}]{cn} Contains immoral and obscene images or texts

    {lrd}[{yw}2{lrd}]{cn} Wasteful consumption of site resources (experimental blogs, spam, contentless or...)

    {lrd}[{yw}3{lrd}]{cn} Insulting people, authorities, religions and racial or religious minorities with vulgar words

    {lrd}[{yw}4{lrd}]{cn} Disclosure of information or private images of people

    {lrd}[{yw}8{lrd}]{cn} Other cases\n\n\n
        {lrd}  Enter Method : {lgn}""")
text_reporter = input(f"{lrd}[{yw}TEXT{lrd}]{cn} Text reporter : {lgn} ")
number = input(f"{lrd}[{yw}TEXT{lrd}]{cn}Enter number report :{lgn} ")
print ("-------------------------------------------------------------")
agent_user = [
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 ',
                        'Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 ',
                        'Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 ',
                        'Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577',
                        'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
                        'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',]
header = {'Host': 'www.blogfa.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length':'1293',
'User-Agent': random.choice(agent_user),
'Connection': 'close'}

payload = {
        "master$ContentPlaceHolderMain$txtUrl":target,
        "cmbType":method,
        "master$ContentPlaceHolderMain$txtMessage":text_reporter,
        "master$ContentPlaceHolderMain$btnSend":"ارسال پیام"}
if method == "1":
        for i in range(int(number)):
                method1 = requests.post("http://www.blogfa.com/report-abuse",data=payload, headers=header)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}Contains immoral and obscene images or texts{lrd}] Number of reports so far : ",i)

elif method == "2":
        for i in range(int(number)):
                method2 = requests.post("http://www.blogfa.com/report-abuse",data=payload, headers=header)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}spam, contentless or..{lrd}] Number of reports so far : ",i)

elif method == "3":
        for i in range(int(number)):
                method3 = requests.post("http://www.blogfa.com/report-abuse",data=payload, headers=header)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}people, authorities, religions and racial or...{lrd}] Number of reports so far : ",i)

elif method == "4":
        for i in range(int(number)):
                method4 = requests.post("http://www.blogfa.com/report-abuse",data=payload, headers=header)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}Disclosure of information or private images of people{lrd}] Number of reports so far : ",i)

elif method == "8":
        for i in range(int(number)):
                method9 = requests.post("http://www.blogfa.com/report-abuse",data=payload, headers=header)
                print ("{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}Other cases{lrd}] Number of reports so far : ",i)              
else:
    print ("ERROR NUMBER ")
