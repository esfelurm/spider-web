import os
import time
import sys,os
os.system("pip install itertools")
os.system("pip install pyuseragents")
import requests as req
import requests
import pyuseragents as a
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'

def banner():
    print (f"""
                                                  
							 {lrd}                                          
									 	     :                   
								   @     	     @                   
								   @     	@    @-                  
								  @      	@    @                  
								 @@      	@@    @@                 
								@@              @@@    @@                
							@     *@@                @@@     @        
						      ##     @@@                  @@@     =@      
						     @+    @@@@    {cn}.          ` {lrd}    @@@@    :@     
						    @@   %@@@@      {cn}%        *{lrd}      #@@@@   @@    
						   .@     *@@@#      {cn}@@%  #@@- {lrd}    +@@@#     @+   
						   @@        @@@     {cn} @@@#@@      {lrd}@@@.      @@   
						   @@         :@@#  {cn}#        *{lrd}  -@@+         @@   
						   @@@@@@@@@@@@%@@% :@@@@@@@@* +@@*@@@@@@@@@@@@   
						   +@@@@@@@@@@@@@@@. @@@@@@@@  @@@@@@@@@@@@@@@%   
						      +*-    +@@@@@@ =@@@@@@% @@@@@@*.   -**      
							     @@@@@@@  @@@@@@  @@@@@@@             
							  :@@@@@@@@@# @@@@@@ -@@@@@@@@@=          
							 @@@@@@*@@@@@ =    - #@@@@*@@@@@@.        
						       %@@@@  +@@@@.           @@@@%  @@@@@       
						      @@@@   *@@@ {pe}   *@@@@@@%{lrd}    @@@%   @@@@      
						      @@@   .@@@    {pe}@@@@@@@@@@{lrd}   @@@=   %@@      
						       @@   @@@    {pe}@@@@-   @@@@{lrd}    @@@   @@.      
						       #@  @@@    {pe}@@@@@@  @@@@@@{lrd}    @@@  @@       
							@: @@.    {pe}@@@@@@  @@@@@@.{lrd}    @@  @        
							@ %@@    {pe}#@@@     .  @@@@{lrd}    @@@ @        
							@ @@@    {pe}@@@@        @@@@{lrd}    %@@ @        
							@ @@:    {pe}@@@@ @@  @@ @@@@{lrd}     @@ %        
						       .  @@     {pe}.@@@@@@  @@@@@@={lrd}     @@  -       
							  @@@     {pe}@@@@@@  *@@@@@{lrd}     @@@          
							  @@@@     {pe}@@@@%@@@@@@@:{lrd}    @@@@          
							    @@@    {pe}:@@@@@@@@@@+{lrd}    @@@            
							     @@.     {pe}@@@@@@@@{lrd}      @@             
							      @@       {pe}@@@@{lrd}       @@              
							      @@        {pe}@@{lrd}        @@              
							      .@         :        @+              
							       @                  @.              
							       @                  %.              
							      ..                   +              
							      @                    @              
							      @                    #              
												  
							     *  
							     
							     
						     {lrd}  github : {lgn}github.com/esfelurm
       
     						     {lrd}  channel Telegram :{lgn} @esfelurm
       	     
{lrd}[{yw}1{lrd}]{lgn} cracker hashing
{yw}--------------------------
{lrd}[{yw}2{lrd}]{lgn} Bug hunter
{yw}--------------------------
{lrd}[{yw}3{lrd}]{lgn} Admin Panel finder and sub
{yw}--------------------------
{lrd}[{yw}4{lrd}]{lgn} Reporter Blogfa		
{yw}--------------------------				
{lrd}[{yw}5{lrd}]{lgn} Reporter Aparat 
{yw}--------------------------
{lrd}[{yw}6{lrd}]{lgn} cracker Blogfa 		

    """)
banner()
Number = input(f"{lrd}[{yw}N{lrd}] {lgn}Enter number : {pe}")
def banner_adminpannel():
    print (f"""
{cn}_______  ______   _______ _________ _         {lgn}  _______  _______  _        _______  _        {lrd}  _______ _________ _        ______   _______  _______ 
{cn}(  ___  )(  __  \ (       )\__   __/( (    /| {lgn} (  ____ )(  ___  )( (    /|(  ____ \( \       {lrd} (  ____ \\__   __/( (    /|(  __  \ (  ____ \(  ____ )
{cn}| (   ) || (  \  )| () () |   ) (   |  \  ( | {lgn} | (    )|| (   ) ||  \  ( || (    \/| (       {lrd} | (    \/   ) (   |  \  ( || (  \  )| (    \/| (    )|
{cn}| (___) || |   ) || || || |   | |   |   \ | | {lgn} | (____)|| (___) ||   \ | || (__    | |       {lrd} | (__       | |   |   \ | || |   ) || (__    | (____)|
{cn}|  ___  || |   | || |(_)| |   | |   | (\ \) | {lgn} |  _____)|  ___  || (\ \) ||  __)   | |       {lrd} |  __)      | |   | (\ \) || |   | ||  __)   |     __)
{cn}| (   ) || |   ) || |   | |   | |   | | \   | {lgn} | (      | (   ) || | \   || (      | |       {lrd} | (         | |   | | \   || |   ) || (      | (\ (   
{cn}| )   ( || (__/  )| )   ( |___) (___| )  \  | {lgn} | )      | )   ( || )  \  || (____/\| (____/\ {lrd}| )      ___) (___| )  \  || (__/  )| (____/\| ) \ \__
{cn}|/     \|(______/ |/     \|\_______/|/    )_) {lgn} |/       |/     \||/    )_)(_______/(_______/ {lrd} |/       \_______/|/    )_)(______/ (_______/|/   \__/
    
    
     	    {lrd}  github : {lgn}github.com/esfelurm
       
       	    {lrd}  channel Telegram :{lgn} @esfelurm
       
    """)



def admin_pabel():
	os.system("clear")
	banner_adminpannel()
	target = input(f"""{lrd}┌──({yw}admin-panel{lgn}㉿spider)-{lrd}[{yw}~{lrd}]{lgn}
└─{lrd}$  Target URL [{lgn}google.com{lrd}] : {pe}""") 
    
	try:	
	    if 'http://' or 'https://' in target:target = 'http://'+target
	    test_url = requests.get(target)
	    if test_url.status_code == 200:
		    pass
	except:
	    print (f"{lrd}[{yw}ERROR{lrd}] failed to connect ! ")

	    sys.exit()
	method = input(f"""
	{yw}-------------------------------
	{lrd}A- {lgn}search subdomains
	
	{lrd}َE-{lgn} search admin panel
	
		
		{lrd}[{yw}N{lrd}] Number method : {pe}""")
	if method == 'a' or method == 'A':
		link_list = open('su.txt', 'r').read().split()
		for List in link_list:
		    f = target+'/'+List
		    req = requests.get(f)
		    if '404' in req.text: print (f'{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ {lgn}{target}{List}{lrd} ]')
		    else: print (f'{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {rd}{target}{List}{lrd} ]')
	if method == 'e' or method == 'E':
		link_list= open('pa.txt', 'r').read().split()
		for List in link_list:
		    s = target+'/'+List
		    req = requests.get(s)
		    if '404' in req.text: print (f'{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ {lgn}{target}{List}{lrd} ]')
		    else: print (f'{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {rd}{target}{List}{lrd} ]')
		    
if Number == '3':
    admin_pabel()
elif Number == '1':
    os.system("python cracker-hash.py")
elif Number == '6':
    os.system("python cracker-blogfa.py")
elif Number == '5':
    os.system("python install reporter-aparat.py")
elif Number == '4':
    os.system("python reporter.py")	
elif Number == '2':
    os.system("python bug.py")

