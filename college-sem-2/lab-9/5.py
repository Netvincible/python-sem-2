def ispangram(Str):
    sentance=set(Str.lower())
    Stall=set("abcdefghijklmnopqrstuvwxyz")

    if sentance>=Stall:
        return True
    else:
        return False

print(ispangram("Abcd Efgh IJkLMnO pQRS tuVwX yZ"))
print(ispangram("Hi Hello My name is Netra"))