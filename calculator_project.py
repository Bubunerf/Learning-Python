


def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

avaiable_operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    continue_with_the_same_or_not = False
    while True:
        
        if continue_with_the_same_or_not == True:
            first_num = current_result
        else:
            first_num = int(input("Please enter the first number?:"))

        
        for symbol in avaiable_operations:
            print(symbol) 


        operation = str(input("Please choose from the following operations "))
        
        second_num = int(input("Please input the second number: "))

        current_result = avaiable_operations[operation](first_num , second_num)

        print(f"{first_num} {operation} {second_num} = {current_result}")

        
        test = input(f"Type 'y' to continue calculating with {current_result} , or type 'n' to start a new calculation: ")
        if test == "y":
            continue_with_the_same_or_not = True
        else:
            current_result = 0


calculator()



