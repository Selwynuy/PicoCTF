"""
Mind your Ps and Qs
Description:
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values
"""
from Crypto.Util.number import long_to_bytes

# Decrypt my super sick RSA:
c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e = 65537

# Since n is so small, we will try to get the p's and q's of n using factordb.com
# Then we get the p and q
p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809

phi = (p - 1) * (q - 1)    # calculates the Euler Totient
d = pow(e,-1,n)
m = pow(c,d,n)
print(long_to_bytes(m))

#FLAG: picoCTF{sma11_N_n0_g0od_55304594}
