import requests
import random, time, os
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
os.system("clear")
print (f"""{lrd}

###   ####  ###    ##   ###   ###   ####  ###   
#  #  #     #  #  #  #  #  #   #    #     #  #  
#  #  ###   #  #  #  #  #  #   #    ###   #  #  
###   #     ###   #  #  ###    #    #     ###   
# #   #     #     #  #  # #    #    #     # #   
#  #  ####  #      ##   #  #   #    ####  #  #  
                                             {cn}   
 ##   ###    ##   ###    ##   ###   
#  #  #  #  #  #  #  #  #  #   #    
#  #  #  #  #  #  #  #  #  #   #    
####  ###   ####  ###   ####   #    
#  #  #     #  #  # #   #  #   #    
#  #  #     #  #  #  #  #  #   #    

     {lrd}  github : {lgn}github.com/esfelurm
       
     {lrd}  channel Telegram :{lgn} @esfelurm
     
""")
target = input(f"{lrd}[{yw}URL{lrd}] {lgn}Enter URL target :{pe} ")
print (f"\n\n{yw}Send the time that you want to report. Example : 2:23\n\n")
times1 = input(f"{lrd}Enter time video : {lgn}")
times2 = input(f"{cn}Enter time video2 : {lgn}")
times3 = input(f"{yw}Enter time video3 : {lgn}")
method = input(f"""
    {lrd}[{yw}1{lrd}]{cn} Improper coverage 
    {lrd}[{yw}2{lrd}]{cn} fake news 
    {lrd}[{yw}3{lrd}]{cn} National security or counter-terrorism considerations 
    {lrd}[{yw}4{lrd}]{cn} Sexual content 

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
                        'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
                        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
                        'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                        'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                        'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',
                        'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                        'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ]

users = (random.choice(agent_user))
header = {'User-Agent': users,'Allow': 'GET, HEAD, OPTIONS, TRACE',
 'Content-Type': 'text/html',
 'Server': 'Microsoft-IIS/8.5',
 'X-Powered-By': 'ARR/3.0, ASP.NET',
 'Content-Length': '1293'}

if method == "1":
        for i in range(int(number)):
                payload = {
        'Set-Cookie':users,
        "videoURL":target,
        "selectbox-item":'پوشش نامناسب',
        "main_time1":times1,
        "main_time2":times2,
        "main_time3":times3,
        "body":text_reporter,
        "submit":"ارسال گزارش"
                }
                method1 = requests.post("https://aparat.com",data=payload)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}Improper coverage {lrd}] Number of reports so far : ",i)

elif method == "2":
        for i in range(int(number)):
                payload = {
        'Set-Cookie':users,
        "videoURL":target,
        "selectbox-item":'اخبار جعلی',
        "main_time1":times1,
        "main_time2":times2,
        "main_time3":times3,
        "body":text_reporter,
        "submit":"ارسال گزارش"
                }
                method2 = requests.post("https://aparat.com",data=payload)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}fake news {lrd}] Number of reports so far : ",i)

elif method == "3":
        for i in range(int(number)):
                payload = {
        'Set-Cookie':users,
        "videoURL":target,
        "selectbox-item":'ملاحظات امنیت ملی یا ضد تروریسم',
        "main_time1":times1,
        "main_time2":times2,
        "main_time3":times3,
        "body":text_reporter,
        "submit":"ارسال گزارش"
                }
                method3 = requests.post("https://aparat.com",data=payload)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}National security or counter-terrorism considerations {lrd}] Number of reports so far : ",i)

elif method == "4":
        for i in range(int(number)):
                payload = {
        'Set-Cookie':users,
        "videoURL":target,
        "selectbox-item":'محتوای تحریک آمیز جنسی',
        "main_time1":times1,
        "main_time2":times2,
        "main_time3":times3,
        "body":text_reporter,
        "submit":"ارسال گزارش"
                }                
                method4 = requests.post("https://aparat.com",data=payload)
                print (f"{yw}[{lrd}SENT{yw}] {lgn}The report has been sent to the site! Report type: {lrd}[{yw}Sexual content {lrd}] Number of reports so far : ",i)
                
else:
    print (f"{lrd}ERROR NUMBER ")
