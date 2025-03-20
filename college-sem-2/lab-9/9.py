def count_alpha_digits(string):
    Dict={"alphabets":0,"digits":0}
    for i in string:
        if i.isalpha():
            Dict["alphabets"]+=1
        elif i.isdigit():
            Dict["digits"]+=1
    return Dict

print(count_alpha_digits("Hi hello 324 my name is netra give me a hi5ve"))