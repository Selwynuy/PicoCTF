# basic-mod1
## Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
## Solution
message.txt
```
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213
```

Code:
```
message = [350,63,353,198,114,369,346,184,202,322,94,235,114,110,185,188,225,212,366,374,261,213]
modded_message = []
for c in message:
  modded_message.append(c%37)

# modded_message = [17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 0, 3, 3, 27, 33, 4, 2, 28]
```

Then we have this Character set that I've created
```
character_set = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','_']
```
We know that the modded message is the indexes of characters in character set, we just need to get each characters

```
initial_flag = []
for i in modded_message:
  initial_flag.append(character_set[i])
print(initial_flag)    # ['R', '0', 'U', 'N', 'D', '_', 'N', '_', 'R', '0', 'U', 'N', 'D', '_', 'A', 'D', 'D', '1', '7', 'E', 'C', '2']

flag = "".join(initial_flag)
print("picoCTF{" + flag + "}")
```
FLAG: picoCTF{R0UND_N_R0UND_ADD17EC2}
