# keepass_getter [![Build Status](https://travis-ci.org/M-Gregoire/keepass_getter.svg?branch=master)](https://travis-ci.org/M-Gregoire/keepass_getter) [![Coverage Status](https://coveralls.io/repos/github/M-Gregoire/keepass_getter/badge.svg?branch=master)](https://coveralls.io/github/M-Gregoire/keepass_getter?branch=master)
keepass_getter allow you to retrieve passwords from your open KeePass database using [KeepassHttp](https://github.com/pfn/keepasshttp).  
This Python module is designed to be easy to be called from bash. It can also be used in a Python package.  

It currently only support searching using an url as it's the only retrieving method I need.  

Feel free to ask me to implement recovering multiple passwords or search by title if you need it.

## Installation
keepass_getter is on pypi !  
`pip install keepass-getter`

## Usage

Two functions are available from `keepass_getter` :
* `getPassword(url, index=0)`
* `showPassword(url, index=0)`

where `url` is the search term, and index (optional) the result number, by default, the first match is returned.

### Bash
` python -c 'from keepass_getter import showPassword; showPassword("mywebsite.com")'`

### Python

``` python3
#!/usr/bin/python3

from keepass_getter import getPassword

myPassword=getPassword("mywebsite.com")

# Use myPassword from here...

```

## Credits

This module is a modification of [python-keepasshttp](https://github.com/jobevers/python-keepasshttp) to better suits my need.

## Donation

This project helped you ? You can buy me a cup of coffee  
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=EWHGT3M9899J6)
