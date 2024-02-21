String = input("Enter a String: ")
count =0

for ch in String:
    count =0
    for ch1 in String:

        if ch == ch1:
            count +=1
        else:
            continue
    print(f"The {ch} occured int {String} in {count} times")
        

