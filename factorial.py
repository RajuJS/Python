def factorial(number):
    if number < 0:
        print("invalid number..")
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
if __name__ == "__main__":
    userInput = int(input("Enter Number to find the factorial:"))
    print(factorial(userInput))