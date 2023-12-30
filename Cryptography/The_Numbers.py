"""
Description:
The numbers... what do they mean?
"""

# Opening the png file, we get these numbers:
numbers = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
# This is just a simple substitution since we know that the first part of the flag is 'PICOCTF'

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

#FLAG: PICOCTF{THENUMBERSMASON}
