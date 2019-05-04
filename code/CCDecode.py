ptxt = input("Please type the passwords:")
for p in ptxt:
    if "a" <= p <= "z":
        print(chr(ord("a") + (ord(p) - ord("a") - 3) % 26), end='')
    elif "A" <= p <= "Z":
        print(chr(ord("A") + (ord(p) - ord("A") - 3) % 26), end='')
    elif 0x4E00 <= ord(p) <= 0x9FA5:
        print(chr(ord(p) - 3), end='')
    else:
        print(p, end='')
