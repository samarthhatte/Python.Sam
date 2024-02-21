String = input("Enter a String: ")
Substring = input("Enter a SubString: ")
 
if Substring in String:
    print(f"{Substring} is present in the {String}")
else:
    print(f"{Substring} is not in the {String}")