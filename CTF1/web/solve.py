import re
from Crypto.Util.number import *

with open("flag.txt.enc", "rb") as file:
 ct = bytes_to_long(file.read())

partial_priv_hex = "6573c8d337cce442647a8a11bcdaf744a404a102818100f45ab61bc6106f792458be4395d3ea267eeb704bac08a0299e0980aae4c6e81dd667f0d0c21f2f98eba6fe1bf18c6497b0a8429048bc077008ca1f1a2e9de157a7a031574ae4056b4e44d9e35dfb61b165ef3a0049cc69bc089412fb156d52961ce25d509d8690a5cd3f4829524cf1bbef91f90e727cb78acaa0d42eafefe9730281803d415340235bac7e1983d7533034fed5d0a6ee576803319229e18a2389593fc0131cc953c26d79050b27710310d1ba69c4aec0c866d1630b850d091ba8087a347238165222a8c44961873e6914d576d40f3d222dbd611d3a8930059829626ce119c96f1e8d189021776362e02c8e1a6ba3629a8d9e9d6a7d936199c8ff54e781028181009803b2d53673d51595320c33b98b1b59158e5ccf06d85ae36928da3df69373a5d453d771d7c254f71a6b4a1c9239d7feb26d0af3fdfbd3d8b3ef22484485fdc16d4bf046311607f508bd369c0744b3330c8a361825d1205a552fe15b08aa793d5ffcc736b6b91755be8946d846160e30efca6d19bac9b1d98b53608d26f0e6d702818067a4fc685e86019d2cf35e197c4732cd91ab65943f309ed6f1919d535ff2fb6d382f37c6b16f9dfac4cf7d03d8867d37fea53748584fd3de6c63310b78e399df221339fb4711d30fdd77df9c0b9d827ded047aedbb412c5452f8e07ec259ee21c77338f4cd257c4443eb494fc141b5f21639a9cb614a4a357f55a44e037b46bb"
e = 65537
delimiters = ["010001", "02820100", "02818100"]

pattern = f"({'|'.join(map(re.escape, delimiters))})"
result = re.split(pattern, partial_priv_hex)

# Remove empty strings and delimiters from the result
result = [sub for sub in result if sub not in delimiters and sub != ""]

# print(result)
print(f"end_of_n: {result[0]}")
print(f"decryption_key(d): {result[1]}")
print(f"prime(p): {result[2]}")
# print(f"prime(q): {result[3]}")
# print(f"dp: {result[4]}")
# print(f"dq: {result[5]}")

d = int(result[1],16)
p = int(result[2],16)
q = int(result[3],16)
dp = int(result[4],16)
dq = int(result[5],16)

#contruction of n
n = p * q

#decryption of message
m = pow(ct,d,n)
print(f"Decrypted Cipher Text as Flag:{long_to_bytes(m)}")

#Decrypted Cipher Text as Flag:b'Hey Bob this is Alice.\nI want to let you know that the Flag is 
#gctf{7hi5_k3y_can_b3_r3c0ns7ruc7ed}\'
