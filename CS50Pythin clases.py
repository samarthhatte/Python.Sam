#ask user for there name
name = input("What is your name ")
#remove white spaces
name = name.strip()
#capitalize user name
name = name.capitalize()

#capitalizing each word of name
name = name.title()

#prints username
print(f"Hello ,{name}")