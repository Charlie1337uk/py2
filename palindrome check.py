wordf = input("Enter a word: ")
wordr = wordf[::-1]

print(wordr)
if wordf == wordr:
    print("palindrome")
else:
    print("not palindrome")