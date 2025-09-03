def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    return False
print(divisible_by_ten(int(input("Enter a number: "))))