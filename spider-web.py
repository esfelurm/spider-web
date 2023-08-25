import os
from platform import uname as name
try:from requests import get
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
{lrd}[{yw}3{lrd}]{lgn} Admin Panel finder
{yw}--------------------------
{lrd}[{yw}4{lrd}]{lgn} subdomain Panel finder
{yw}--------------------------
{lrd}[{yw}5{lrd}]{lgn} Reporter Blogfa		
{yw}--------------------------				
{lrd}[{yw}6{lrd}]{lgn} cracker Blogfa 		

    """)
banner()
Number = input(f"{lrd}[{yw}N{lrd}] {lgn}Enter number : {pe}")

def sub():
    target = input(f"""
    
{lrd}+-++-++-++-++-++-++-++-++-++-+
{rd}|{lgn}s{yw}||{lgn}u{yw}||{lgn}b{yw}||{lgn}d{yw}||{lgn}o{yw}||{lgn}m{yw}||{lgn}a{yw}||{lgn}i{yw}||{lgn}n{yw}||{lgn}s{rd}|
{lrd}+-++-++-++-++-++-++-++-++-++-+
		{lrd}  github : {lgn}github.com/esfelurm

{lrd}[{lgn}+{lrd}] {gn}Enter URL Target {cn}[Ex : https://google.com] {gn}: {lgn}""")     
    link_list = open('file/sub.txt', 'r').read().split()
    for List in link_list:
          f = target+'/'+List
          req = get(f)
          if '404' in req.text: 
                print (f'\n{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {lrd}{target}/{cn}\033[41m{List}\033[0m{lrd} ]')
          else:
                print (f'\n{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ \033[42m{target}/{List}\033[0m{lrd} ]')
                        
def admin():
    target = input(f"""{lgn}
 _______  ______   _______ _________ _       
(  ___  )(  __  \ (       )\__   __/( (    /|
| (   ) || (  \  )| () () |   ) (   |  \  ( |
| (___) || |   ) || || || |   | |   |   \ | |
|  ___  || |   | || |(_)| |   | |   | (\ \) |	{lrd}  github : {lgn}github.com/esfelurm
| (   ) || |   ) || |   | |   | |   | | \   |
| )   ( || (__/  )| )   ( |___) (___| )  \  |
|/     \|(______/ |/     \|\_______/|/    )_)

{lrd}[{lgn}+{lrd}] {gn}Enter URL Target {cn}[Ex : https://google.com] {gn}: {lgn}""")     
    link_list = open('file/admin.txt', 'r').read().split()    
    for List in link_list:
           s = target+'/'+List
           req = get(s)
           if '404' in req.text: 
                        print (f'\n{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {lrd}{target}/{cn}\033[41m{List}\033[0m{lrd} ]')
           else: 
                  print (f'\n{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ \033[42m{target}/{List}\033[0m{lrd} ]')
		        	  		    

if Number == '1':
    os.system("python src/cracker-hash.py")
elif Number == '2':
    os.system("python src/bug.py")
elif Number == '3':
    admin()
elif Number == '4':
    sub()
elif Number == '5':
    os.system("python src/reporter.py")	
elif Number == '6':
    os.system("python src/cracker-blogfa.py")
