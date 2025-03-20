def isPalindrome(string):
    string=string.replace(" ","").lower()
    
    return True if(string[:int(len(string)/2):]==string[:-int(len(string)/2)-1:-1]) else False

String="HihIh"
print(isPalindrome(String))