# The Numbers

## Description
The numbers... what do they mean?

## Solution
png file:

<img width="387" alt="the_numbers" src="https://github.com/Selwynuy/PicoCTF/assets/107299589/605f36ae-3b66-4d6d-b3cc-df0ade715258">

This is just a simple substitution since we know that the first part of the flag is 'PICOCTF'

```
def convert_to_alphabet(decimal_number):
    if 1 <= decimal_number <= 26:
        return chr(ord('A') + decimal_number - 1)
    else:
        return "Number out of range for the alphabet conversion"

initial_flag = []
for c in numbers:
  text = convert_to_alphabet(c)
  initial_flag.append(text)

final_flag = "".join(initial_flag)
print(final_flag)                          # Output: PICOCTFTHENUMBERSMASON
```
#FLAG: PICOCTF{THENUMBERSMASON}
