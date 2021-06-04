<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbgsg-LEnF3j_K6yrP0HyZxZe_hR4rpks8LQ&usqp=CAU" align="right" width="90" height="80">

# WpCrack Tool

![Python](https://img.shields.io/badge/Python-3.9.2-blue)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

![Terkey](https://github-readme-stats.vercel.app/api/pin?username=RandsX&repo=xmlrpc-brute-force-wordpress&title_color=000&icon_color=000&text_color=000000&bg_color=ffffff)

> WordPress Brute Force Super Fast Login

```
      .---.        .-----------
     /     \  __  /    ------
    / /     \(  )/    -----
   //////   ' \/ `   ---
  //// / // : ★★ : ---
 // /   /  /`    '--
//          //..\   WpCrack Brute Froce Tool™
       ====UU====UU==========================
           '//||\`
             ''``
usage: python WpCrack.py [options]                              
optional arguments:
  -h, --help        show this help message and exit
  -V, --version     show program's version number and exit
  -d, --debug       debugging mode

target arguments:
  -t , --target     url of the target
  -u , --username   username of the target (default: admin)
  -p , --password   password of the target (change -p to --p to use a wordlist)

  --timeout         timed out for requests
  --thread          numbers of threading multiproccesor (default: 5)
  --proxy           using a HTTP proxy (ex: http://site.com:8000)

Copyright © 2021 Andrew - Powered by Indonesian Darknet
```

## How To Use

Using a single password
```bash
python WpCrack.py -t http://site.com/wp-login.php -u admin -p password
```

Using a multiple password / wordlist
```bash
python WpCrack.py -t http://site.com/wp-login.php -u admin --p wordlist.txt
```

## About
WpCrack is a tool used to force login into the WordPress CMS web application and is built in the Python programming language

## Features
- Very fast login
- Use of HTTP proxies
- Multithreading or Multiprocessor
