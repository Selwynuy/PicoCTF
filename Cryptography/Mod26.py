"""
Description:
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}
"""

from codecs import encode

text = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"

print(encode(text, 'rot_13'))

#FLAG: picoCTF{next_time_I'll_try_2_rounds_of_rot13_hWqFsgzu}
