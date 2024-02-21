def main():
    size  = int(input("Enter the size of bricks: "))
    build_the_brick(size)
    
    
def build_the_brick(height):
    for width in range(height):
        print("#" * height)
    
main()