def isVowel(x):
    vowels = "aeiouAEIOU"
    return x in vowels

def updateSandwichedVowels(a):
    n = len(a)
    updatedString = ""
    
    for i in range(n):
        if i == 0 or i == n - 1:
            updatedString += a[i]
            continue
        
        if isVowel(a[i]) and not isVowel(a[i - 1]) and not isVowel(a[i + 1]):
            continue
        
        updatedString += a[i]
    
    return updatedString

# Taking user input
user_input = input("Enter a string: ")

# Applying the function to remove sandwiched vowels
result = updateSandwichedVowels(user_input)

# Outputting the modified string
print(f"String after updating sandwiched vowels: {result}")
