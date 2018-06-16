# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
# import string
# s = string.ascii_uppercase # 65 a 90
# s = string.ascii_lowercase # 97 a 122
# s = "A vamos testar <br>!$"

s="áâãà"
def ROT13 (s = ""):
    t  = ""
    
    for c in s:
        o = ord(c)
        if (o > 96 and o < 123):
            o += 13
            if (o > 122):
                o -= 26
        if (o > 64 and o < 91):
            o += 13
            if (o > 90):
                o -= 26
        t += chr(o)
                
    return t
    
d = (ord("á"))

print(chr(d))