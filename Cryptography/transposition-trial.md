# transposition-trial
## Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message here.
## Solution
message.txt
```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2
```
The first word seems to be 'The' and the second word seems to be 'flag'

I then created a code to unscramble these scrambled letters

```
message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

message_block_list = []

for index in range(0, len(message), 3):
  block = list(message[index:index+3])
  block[0], block[1], block[2] = block[2], block[0], block[1] 
  message_block_list.append(''.join(block))

flag = ''.join(message_block_list)
print(flag)
```
Flag: picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}
