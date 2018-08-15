# WikiRider
##
Do a Wikirun directly from your terminal ( assuming you use Linux or Mac )!<br />
[![Travis](https://img.shields.io/travis/sadboyzvone/wikirider.svg)](https://github.com/sadboyzvone/8080py)
[![Known Vulnerabilities](https://snyk.io/test/github/sadboyzvone/wikirider/badge.svg)](https://snyk.io/test/github/sadboyzvone/wikirider)
[![Code Climate](https://img.shields.io/codeclimate/coverage/github/sadboyzvone/wikirider.svg)](https://github.com/sadboyzvone/8080py)

## Install

### Debian-based distros
```bash
# Clone the repo
git clone git@github.com:sadboyzvone/wikirider.git
# Install virtualenv
sudo pip install virtualenv
# Create a virtualenv
cd wikirider && virtualenv .
# Activate virtualenv
source bin/activate
# Install requirements
pip install -r requirements.txt
```

### Windows
Enter the following in administrator mode.
```
git clone git@github.com:sadboyzvone/wikirider.git
pip install virtualenv
cd wikirider
virtualenv .
Scripts\activate
```
Before installing any packages, lxml should be installed by using a precompiled
wheel [Download] (https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml).
```
pip install lxml-4.X.X-cpXX-cpXXm-winX.whl
pip install -r requirements_windows.txt
```
At the moment of writing, having 64-bit python installed is necessary to
run the interactive GUI.

## Run
```bash
python main.py
```

## FAQ:
* What is a Wikirun?
	* [This](http://www.urbandictionary.com/define.php?term=Wikirun)
* Does it work on XYZ OS?
	* If you have Python on it, it probably will
