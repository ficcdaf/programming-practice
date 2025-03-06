# up = "ABCDEFGH"
# low = "abcdefgh"
inp = "hElO"
def process(string, command):
    if command == "up":
        pass
    elif command == "low":
        pass
    elif command == "swap":
        pass
    else:
        print("Not a real command!")

def isPalindrome(word):
    rev = ""
    rev2 = ""
    for i in reversed(range(len(word))):
        rev += word[i]
    for c in reversed(word):
        rev2 += c
    print(rev)
    print(rev2)
    return rev == word
print(isPalindrome("civic"))
