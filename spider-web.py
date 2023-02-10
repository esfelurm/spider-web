import os
import time
import sys,os
os.system("pip install itertools")
os.system("pip install pyuseragents")
import requests as req
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
       	     
							                         .             
												  
               {lrd}[{yw}1{lrd}]{lgn} cracker hashing					{lrd}[{yw}2{lrd}]{lgn} Bug hunter
               
               
               {lrd}[{yw}3{lrd}]{lgn} Admin Panel finder and sub			        {lrd}[{yw}4{lrd}]{lgn} Reporter Blogfa						
               
              
               {lrd}[{yw}5{lrd}]{lgn} Reporter Aparat            		                             {lrd}[{yw}6{lrd}]{lgn} cracker Blogfa 					
               
               					
                                                  

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
	if 'http://' or 'https://' not in target:
	    target = 'http://'+target
	try:	
	    test_url = req.get(target)
	    if test_url.status_code == 200:
		    pass
	except:
	    print (f"{lrd}[{yw}ERROR{lrd}] failed to connect ! ")
	    sys.exit()
	method = input(f"""
	{yw}-------------------------------
	{lrd}1- {lgn}search subdomains
	
	{lrd}2-{lgn} search admin panel
	
		
		{lrd}[{yw}N{lrd}] Number method : {pe}""")
	if method == 'a' or method == 'A':
	    link_list = open('su.txt', 'r').read().split()
	    for line_list in link_list:
                try:
                    url = ('http://'+line_list+'.'+target)
                    get_req = req.get(url)
                    print(f'{lrd}[{lgn}OK{lrd}]{lgn} Admin panel found : {lrd}[ {lgn}'+url+f'{lrd} ]')
                except Exception:
                    print(f'{lrd}[{yw}NO{lrd}] {lrd}Admin panel not found : {lrd}[ {rd}'+url+f'{lrd} ]')
                
                except KeyboardInterrupt:
                    sys.exit()
	if method == 'e' or method == 'E':
	    link_list= open('pa.txt', 'r').read().split()
	    for line_list in link_list:
	        try:
	            url = ('http://'+target+'/'+line_list)
	            get_req = req.get(url)
	            print(f'{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ {lgn}'+url+f'{lrd} ]')
	        except Exception:
	            print(f'{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {rd}'+url+f'{lrd} ]')
	            
	        except KeyboardInterrupt:    
	            sys.exit()
	else:
	    print(f"{lrd}[{yw}ERROR{lrd}] The desired page is not available !")
	    sys.exit()
	target = target.replace('http://', '')

if Number == '3':
    admin_pabel()
elif Number == '1':
    os.system("python cracker-hash.py")
elif Number == '6':
    os.system("python cracker-blogfa.py")
elif Number == '5':
    os.system("pip install reporter-aparat.py")
elif Number == '4':
    os.system("python reporter.py")	
elif Number == '2':
    os.system("python bug.py")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

