import string

def ispangram(s, alphabet=string.ascii_lowercase):
    s = s.replace(" ","")
    s_set = set(s)
    for i in alphabet:
        if i in s_set:
            continue
        else:
            return False
    return True
  
print(ispangram("abb c d eeeef gh"))
print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("abcdefghijklmnopqrstuvwxyz"))
