<h1 align="center">WordPress Crack<br/>Super Fast Login</h1>

> this is the first version, we will fix any bugs that appear. so expect participation :)

```
WordPress Brute Force Super Fast Login By 22XploiterCrew
Website : https://22xploitercrew.my.id
E-Mail  : dev@22xploitercrew.my.id

usage: python3 wp-crack.py url username [-p|-P] [-v VERBOSE]

positional arguments:
  url               url the target
  username          username target

optional arguments:
  -h, --help        show this help message and exit
  -V, --version     show program's version number and
                    exit
  -v, --verbose     verbose mode/show username and
                    password combination for each attempt
  -p , --password   use one word password
  -P , --passlist   use a few words password

Please check your target first so that the login process
runs smoothly
```

### Required
- Python3

### How To Use
- Single password
```
python3 wp-crack.py https://site.com/wp-login.php username -p password
```

- List password
```
python3 wp-crack.py https://site.com/wp-login.php username -P password.txt
```
