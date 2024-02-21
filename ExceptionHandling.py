
def main():
    x = get_int("What's x? ")
    print(f"X is {x}")
    
    
def  get_int(promt):  
    while True:
     try:
       return int(input(promt))
     except ValueError:
        pass


main()