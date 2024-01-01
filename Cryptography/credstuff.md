# credstuff
## Description
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.
## Solution
You will be given a usernames.txt and a passwords.txt

since it is a one to one basis, I can get the password by getting the line of the username 'cultiris'


Using this command:
```
$ cat usernames.txt | grep -n 'cultiris'
# \378:cultiris
```
It says at line 378, 'cultiris' is found, then it must be at line 378 is the password for username cultiris is.

Using head and tails command to get that specific line
```
head -n 378 passwords.txt | tail -1
# cvpbPGS{P7e1S_54I35_71Z3}
```
Then use tools like cyberchef to get the flag using rot cipher (rot13)

Flag: picoCTF{C7r1F_54V35_71M3}
