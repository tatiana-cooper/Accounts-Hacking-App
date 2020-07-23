
# Hacking user accounts App 

*The program, through various manipulations and functions, performs attempts to hack user's accounts*

![image](https://drive.google.com/uc?export=view&id=1jSjX5HAXOvVdR-prZ8byYnFLygoXpsXz)

In this project I mastered:

**Python** <br>
**Flask** <br>
**Requests**<br>
**Various enumeration algorithms**<br>


## Files

> server.py — this file runs Flask server and processes requests to the server.

> generators.py — this file forms passwords and usernames for hacking.

> logic.py — functions in this file coordinate work of program depending on the chosen function (functions based on different logics).

> main.py — is the main file to launch app. In this file,  User should choose parameters of hacking-app corresponding to his needs.

> queries.py — this file sends requests to the server with password and username. In this file's function, a request was adjusted for a self-created server (server.py) and self-created users (users.json).

> 10-million-password-list-top-1000000.txt — the file consists of the top 10 million most popular passwords. Was taken from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt.

> top-10-million-usernames.txt — the file consists of the top 10 million most popular usernames. Was taken from 
https://github.com/danielmiessler/SecLists/blob/master/Usernames/xato-net-10-million-usernames-dup.txt.

> users.json — the file consists of the server's self-created usernames and corresponding passwords.

## Installation
App requires Python 3+.

### Clone

Clone this repo to your local machine using  `https://github.com/tatiana-cooper/Accounts-Hacking-App.git`

### Setup
Windows 10:

For launching server:
```sh
> python server.py
```
For launching App (in this file you should choose parameters of hacking):
```sh
> python main.py
```

## Features
Hacking techniques:
- Brute Force attack
- Enumeration of the top 10 million most popular usernames
- Enumeration of the top 10 million most popular passwords
---
 *This project was created during "Cracking and Brute Force attacks in Python" intensive classes by Skillbox University.*
