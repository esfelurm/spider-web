import hashlib,os,sys,time,random
import time, os
from itertools import product
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
os.system("clear")
class STARTING:

    def Random(self,charectors,min,max,limit):
        char = list(set(list(charectors)))
        for i in range(limit):
            word = ""
            for ii in range(random.randint(min,max)):
                random.shuffle(char)
                word=word+str(char[0])
            yield word

    def crackin(self,my_str,min,max):
        for i in range(min,max+1):
            for w in product(my_str,repeat=i):
                word = "".join(w)
                yield word
     
            
    def DICT(self,file_name_or_path):
        f = open(file_name_or_path,"r")
        pass_list = f.readlines()
        f.close()
        for i in pass_list:
            word = i.replace("\n","")
            yield word

class cheching:
    def hash_key(self,NAME_H4SH,key_hash,num):
        HASHI = G4N(key_hash)
        if num == "1":
            if HASHI.md5() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="2":
            if HASHI.sha1() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="3":
            if HASHI.sha224() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="4":
            if HASHI.sha256() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="5":
            if HASHI.sha384() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="6":
            if HASHI.sha512() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="7":
            if HASHI.blake2b() == NAME_H4SH:
                return True
            else:
                return False
        elif num =="8":
            if HASHI.blake2s() == NAME_H4SH:
                return True
            else:
                return False

class G4N:

    def __init__(self,INP):
        self.hash_str = INP 
    def md5(self):
        return hashlib.md5(self.hash_str.encode('utf-8')).hexdigest()
    def sha1(self):
        return hashlib.sha1(self.hash_str.encode('utf-8')).hexdigest()
    def sha224(self):
        return hashlib.sha224(self.hash_str.encode('utf-8')).hexdigest()
    def sha256(self):
        return hashlib.sha256(self.hash_str.encode('utf-8')).hexdigest()
    def sha384(self):
        return hashlib.sha384(self.hash_str.encode('utf-8')).hexdigest()
    def sha512(self):
        return hashlib.sha512(self.hash_str.encode('utf-8')).hexdigest()
    def blake2b(self):
        return hashlib.blake2b(self.hash_str.encode('utf-8')).hexdigest()
    def blake2s(self):
        return hashlib.blake2s(self.hash_str.encode('utf-8')).hexdigest()



class CRC:
    def __init__(self):
        self.gen = STARTING()
        self.key_hash = cheching()
        
        self.BANNER = f"""{lrd}
{lgn}   _,.----.                    ,---.         _,.----.    ,--.-.,-.       ,----.                {lrd}   ,--.-,,-,--,    ,---.         ,-,--.   ,--.-,,-,--, 
{lgn} .' .' -   \    .-.,.---.    .--.'  \      .' .' -   \  /==/- |\  \   ,-.--` , \   .-.,.---.   {lrd}  /==/  /|=|  |  .--.'  \      ,-.'-  _\ /==/  /|=|  | 
{lgn}/==/  ,  ,-'   /==/  `   \   \==\-/\ \    /==/  ,  ,-'  |==|_ `/_ /  |==|-  _.-`  /==/  `   \  {lrd}  |==|_ ||=|, |  \==\-/\ \    /==/_ ,_.' |==|_ ||=|, | 
{lgn}|==|-   |  .  |==|-, .=., |  /==/-|_\ |   |==|-   |  .  |==| ,   /   |==|   `.-. |==|-, .=., | {lrd}  |==| ,|/=| _|  /==/-|_\ |   \==\  \    |==| ,|/=| _| 
{lgn}|==|_   `-' \ |==|   '='  /  \==\,   - \  |==|_   `-' \ |==|-  .|   /==/_ ,    / |==|   '='  / {lrd}  |==|- `-' _ |  \==\,   - \   \==\ -\   |==|- `-' _ | 
{lgn}|==|   _  , | |==|- ,   .'   /==/ -   ,|  |==|   _  , | |==| _ , \  |==|    .-'  |==|- ,   .'  {lrd}  |==|  _     |  /==/ -   ,|   _\==\ ,\  |==|  _     | 
{lgn}\==\.       / |==|_  . ,'.  /==/-  /\ - \ \==\.       / /==/  '\  | |==|_  ,`-._ |==|_  . ,'.  {lrd}  |==|   .-. ,\ /==/-  /\ - \ /==/\/ _ | |==|   .-. ,\ 
{lgn}`-.`.___.-'  /==/  /\ ,  ) \==\ _.\=\.-'  `-.`.___.-'  \==\ /\=\.' /==/ ,     / /==/  /\ ,  )  {lrd} /==/, //=/  | \==\ _.\=\.-' \==\ - , / /==/, //=/  | 
{lgn}              `--`-`--`--'   `--`                        `--`       `--`-----``  `--`-`--`--'  {lrd}  `--`-' `-`--`  `--`          `--`---'  `--`-' `-`--` 
        """
    def clear(self):
        os.system("clear")
    def NEW_START(self):
        main.clear()
        print(self.BANNER)
 
        bNAME_H4SH =input(f"{lrd}[{yw}HASH{lrd}]{lgn} Enter hash : {cn}").replace("'","").replace('"',"").lstrip().rstrip()
        hash_type = input(f"""{yw}
-------------------------------------------------------------------        
|                                                                  |
|        {lrd}[{yw}1{lrd}]{pe} MD5{yw}                             		           |
|                                                                  |
|        {lrd}[{yw}2{lrd}]{pe} SHA1{yw}                          			   |
|                                                                  |
|        {lrd}[{yw}3{lrd}]{pe} SHA224 {yw}                			           |
|                                                                  |
|        {lrd}[{yw}4{lrd}]{pe} SHA256  {yw}              			           |
|                                                                  |
|        {lrd}[{yw}5{lrd}]{pe} SHA384  {yw}                			           |
|                                                                  |
|        {lrd}[{yw}6{lrd}]{pe} SHA512  {yw}                  			           |
|                                                                  |
|        {lrd}[{yw}7{lrd}]{pe} BLAKE2B  {yw}               			           |
|                                                                  |
|        {lrd}[{yw}8{lrd}]{pe} BLAKE2S   {yw}                			           |
|                                                                  |
------------------------------------------------------------------       		
			
		{cn}Number hash :{lgn} """)
        b_str = input(f"{lrd}[{yw}PS{lrd}] {lgn}Enter a keyword, Such as [Admin] : {pe}")
        print (f"{lrd}----------------------------------------------------------------------------")        
        b_min = int(input(f"{lrd}[{yw}NUMBER{lrd}] {lgn}Enter the minimum password length, Suggestion [0] : {pe}"))
        print (f"{lrd}----------------------------------------------------------------------------")
        b_max = int(input(f"{lrd}[{yw}NUMBER{lrd}] {lgn}Enter the maximum password length, Suggestion [10] : {pe}"))
        
        
        for i in self.gen.crackin(b_str,b_min,b_max):
    
            print (f"{yw}[{lrd}FALSE{yw}] Test key : {cn}", i)
            if self.key_hash.hash_key(bNAME_H4SH,str(i),hash_type) == True:
                time.sleep(3)
                print (f"""{lrd}
--------------------------------------------------------------------------------------------
						                          {lrd}   #  
		{pe}	 ####  #####    ##    ####  #    # ###### #####   {lrd}  ### 		  Hash Target :{lgn}{bNAME_H4SH}
		{pe}	#    # #    #  #  #  #    # #   #  #      #    #  {lrd}   #  
		{pe}	#      #    # #    # #      ####   #####  #    #          	          Hash type : {lgn}{hash_type}
		{pe}	#      #####  ###### #      #  #   #      #    #  {lrd}   #  
		{pe}	#    # #   #  #    # #    # #   #  #      #    #  {lrd}  ### 		  Password : {lgn}{i}
		{pe}	 ####  #    # #    #  ####  #    # ###### #####   {lrd}   #  
		

---------------------------------------------------------------------------------------------         
                """)
                sys.exit()
               
               
        
            else:
                pass
        
        main.NEW_START()
                

while True:
    try:
        main = CRC()
        main.NEW_START()
    except KeyboardInterrupt:
        pass        
            
