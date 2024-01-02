# HideToSee
## Description
How about some hide and seek heh?
Look at this image here.
## Solution
You get a file 'atbash.jpg'
```
$ steghide extract -sf atbash.jpg
Enter passphrase:
wrote extracted data to "encrypted.txt"
$ cat encrypted.txt
krxlXGU{zgyzhs_xizxp_8z0uvwwx}
```
Use online tool to decipher the message: https://www.dcode.fr/atbash-cipher

Flag: picoCTF{atbash_crack_8a0feddc}
