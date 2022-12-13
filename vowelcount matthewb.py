stringystring = input("What's your string? ")
vowels = ["a", "e", "i", "o", "u"]
vowelcount = 0
stringystring = stringystring.lower()

for character in stringystring:
    if character in vowels:
        vowelcount += 1
    else:
        continue
print("There are", vowelcount, "vowels in your string!")