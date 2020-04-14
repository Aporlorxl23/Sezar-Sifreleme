# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:01:27 2020

@author: Aporlorxl23
"""
def Encrypt(Text, Key):
    EncryptText = ""
    for i in Text:
        EncryptText = EncryptText + chr(ord(i) + Key)
    print("[+] Key>>",str(Key) + " Encrypt Text>>",EncryptText)
def Decrypt(Text, Key):
    DecryptText = ""
    for i in Text:
        DecryptText = DecryptText + chr(ord(i) - Key)
    print("[+] Key>>",str(Key) + " Decrypt Text>>",DecryptText)
def Brute(Text):
    DecryptText = ""
    Key = 1
    while Key < 26:
        for i in Text:
            DecryptText = DecryptText + chr(ord(i) - Key)
        print("[+] Key>>",str(Key) + " Decrypt Text>>",DecryptText)
        Key += 1
        DecryptText = ""
print("""
[01] Encrypt
[02] Decrypt
[03] Decrypt With Bruteforce
[99] Exit
""")
Option = int(input("Option>> "))
if Option == 99:
    print("[-] Exit...")
    exit
elif Option == 1:
    Text = input("[+] Text>> ")
    Key = int(input("[+] Key>> "))
    Encrypt(Text, Key)
elif Option == 2:
    Text = input("[+] Text>> ")
    Key = int(input("[+] Key>> "))
    Decrypt(Text, Key)
elif Option == 3:
    Text = input("[+] Text>> ")
    Brute(Text)
else:
    print("[?] Please Select Options !")
    exit