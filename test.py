products = 12 
def calulate_product(numbers):
    product =1
    for num in numbers:
        product *= num
    return product
numbers = [2,3,4,5]
product_result = calulate_product(numbers)+10
print(f"The product is :{product_result}")