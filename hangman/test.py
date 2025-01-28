word = "apple"
correct = ['e', 'a', 'p', 'l']

output = ""
for char in word:
    if char in correct:
        output += char
    else:
        # missing = True
        output += '_'
if '_' not in output:
    print("you win!")
print(output)

