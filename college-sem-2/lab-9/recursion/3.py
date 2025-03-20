vowel=['a','e','i','o','u']
def vowels(string,count=0):
    try:
        vowel.index(string[0])
        count+=1
    except ValueError:
        pass

    if (len(string)>1):
        return vowels(string[1:],count)
    else:
        return count

print(vowels("netra"))

