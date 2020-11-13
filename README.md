<h1 align="center">WordPress<br/>Super Fast Login v1.3</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9.0-brightgreen">
  <img src="https://img.shields.io/badge/Languange-English-yellowgreen">
  <img src="https://img.shields.io/badge/License-CC-red">
</p>

> ***Do the login process very quickly.*** <br>Wordlist over 100 words only takes about 10-15 seconds if successful sign in the target

```
WordPress Brute Force Fast Login
Author : RandsX@22XploiterCrew
E-Mail : dev@22xploitercrew.my.id

usage: python3 wp-crack.py url username [-p|-P] [-x PROXY] [-v VERBOSE]

positional arguments:
  url               url the target
  username          username target

optional arguments:
  -h, --help        show this help message and exit
  -V, --version     show program's version number and exit
  -v, --verbose     verbose mode/show username and password
                    combination for each attempt
  -p , --password   use one word password
  -P , --passlist   use a few words password
  -x , --proxy      use a socks/proxy for request (ex:
                    127.0.0.1:8080)

Please check your target first so that the login process runs
smoothly
```

## Installation
This tool requires a module, some of which are :
```
Package                   Version
------------------------- ---------
colorama                  0.4.4
requests                  2.24.0
urllib3                   1.25.11
```

Please check the modules you have installed by typing ```pip3 list```, if there is a module name and version that is required then you don't need to install the module
but if there is no required module, then type this in your terminal

```
pip3 install -r requirements.txt
```

## What's new in version 1.3?
- Add tool logo
- Detect captcha (***the system will automatically stop if the target brings up a captcha***)
- Displays the duration of time when successful login

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