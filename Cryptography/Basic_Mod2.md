# basic-mod2
## Description
A new modular challenge!
Download the message here.
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
## Solution
message.txt
```
104 372 110 436 262 173 354 393 351 297 241 86 262 359 256 441 124 154 165 165 219 288 42
```
Code:
```
message = [104,372,110,436,262,173,354,393,351,297,241,86,262,359,256,441,124,154,165,165,219,288,42]
modded_message = []
for c in message:
  modded_message.append(c%41)
print(modded_message)

# modded_message = [22, 3, 28, 26, 16, 9, 26, 24, 23, 10, 36, 4, 16, 31, 10, 31, 1, 31, 1, 1, 14, 1, 1]
```
Next, we will try to find the modular inverse of the result
```
# modular inverse is pow(m,-1,n)
# we know that n is 41
# we now just need to solve for the modular inverse of each characters in the modded messge

modular_inversed = []
for k in modded_message:
  modular_inversed.append(pow(k,-1,41))
print(modular_inversed)

# modular_inversed = [28, 14, 22, 30, 18, 32, 30, 12, 25, 37, 8, 31, 18, 4, 37, 4, 1, 4, 1, 1, 3, 1, 1]
```
Then we have this character set i've created
```
character_set = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
```
We know that the 'modular_inversed' is the indexes of characters in character set, we just need to get each characters
```
initial_flag = []
for i in modular_inversed:
  initial_flag.append(character_set[i])
print(initial_flag)    

flag = "".join(initial_flag)
print("picoCTF{" + flag + "}")
```
Flag: picoCTF{1NV3R53LY_H4RD_DADAACAA}
