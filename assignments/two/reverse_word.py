def rev_str(string):
    new_str = ""
    for i in range(len(str), -1, -1, -1):
        new_str += string[i]
    return new_str

print(rev_Str("swa"))