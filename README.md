<h1 align="center">WordPress<br/>Super Fast Login v1.4</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9.0-brightgreen">
  <img src="https://img.shields.io/badge/Languange-English-yellowgreen">
  <img src="https://img.shields.io/badge/License-CC-red">

![Terkey](https://github-readme-stats.vercel.app/api/pin?username=RandsX&repo=Terkey&title_color=fff&icon_color=f9f9f9&text_color=9f9f9f&bg_color=151515)
![Shell Backdoor](https://github-readme-stats.vercel.app/api/pin?username=22XploiterCrew-Team&repo=Shell-Backdoor&title_color=fff&icon_color=f9f9f9&text_color=9f9f9f&bg_color=151515)

</p>

> ***Do the login process very quickly.*** <br>Wordlist over 100 words only takes about 10-15 seconds if successful sign in the target

```
 _    _       _____                _
| |  | |     /  __ \              | |
| |  | |_ __ | /  \/_ __ __ _  ___| | __  _ __  _   _
| |/\| | '_ \| |   | '__/ _` |/ __| |/ / | '_ \| | | |
\  /\  / |_) | \__/\ | | (_| | (__|   < _| |_) | |_| |
 \/  \/| .__/ \____/_|  \__,_|\___|_|\_(_) .__/ \__, |
       | |                               | |     __/ |
       |_|                               |_|    |___/
Brute Force WordPress tool with fast login features and multiple login methods.
author: 22XploiterCrew
homepage: https://22xploitercrew.org
github: https://github.com/22XploiterCrew-Team

usage: use "python3 wpcrack.py -h/--help" for more information

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and
                        exit
  -s, --show            show login process
  --timeout TIMEOUT     set timed out request
  --proxies PROXY       use a proxies in the request
  -mt {default,xmlrpc}  method login (default "default")

target:
  if you want to use a wordlist of each of these
  arguments, add the letter "f" behind the argument
  (ex: "-pf password.txt"). NOT FOR TARGET

  -t , --target         target url link (ex.
                        https://site.com/)
  -u , --username       insert a username for the target
  -p , --password       insert a password for the target
```

## Installation
This tool requires a module, some of which are :
```
Package                   Version
------------------------- ---------
colorama                  0.4.4
requests                  2.24.0
urllib3                   1.25.11
bs4                       0.0.1
```

Please check the modules you have installed by typing ```pip3 list```, if there is a module name and version that is required then you don't need to install the module
but if there is no required module, then type this in your terminal

```
pip3 install -r requirements.txt
```

## What's new in version 1.4?
- Detect captcha (***the system will automatically stop if the target brings up a captcha***)
- Displays the duration of time when successful login
- New display
- Change command argument
- Add wordlist for username
- Double checking target
- Multi method (default, xmlrpc)

<!-- AUTO-GENERATED-CONTENT:START (TOC:collapse=true&collapseText="Click to expand") -->
<details>
<summary>Updates in previous versions "Click to view"</summary>

- Fixed bugs
- Added a proxy feature for requests
- Using the new module ```requests``` and ```colorama```
- Easy to use
- Multiprocessing

</details>
<!-- AUTO-GENERATED-CONTENT:END -->

## How to use
Type this in your terminal ```python3 wp-crack.py -h/--help``` for more information. <br>
The super fast login feature is only available if you guess (brute force) the target using a wordlist password.
- Single password

```
Without proxy
python3 wp-crack.py https://site.com/wp-login.php username -p password

With proxy
python3 wp-crack.py https://site.com/wp-login.php username -p password -x http://127.0.0.1:8000
```

- List/multi passwords

```
Without proxy
python3 wp-crack.py https://site.com/wp-login.php username -P password.txt

With proxy
python3 wp-crack.py https://site.com/wp-login.php username -P password.txt -x http://127.0.0.1:8000
```

if you wish to display the password and username that was attempted to sign in into the target, use option ```-v/--verbose```

## Attention
If you find an error, please report here using menu ```Issues``` or can contribute directly with us

<h1 align="center">DON'T FORGET TO STAR</h1>
