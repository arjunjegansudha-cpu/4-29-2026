string=input("Please enter your string:")
reverse=("")
for i in string:
    reverse=i+reverse
print("The original string:", string)
print("The reversed string:", reverse)