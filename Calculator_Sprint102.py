def calculate(text_input):
    if "+" in text_input:
        new_text_input = text_input.split("+")
        num1 = int(new_text_input[0])
        num2 = int(new_text_input[1])
        return num1 + num2

    elif "-" in text_input:
        new_text_input = text_input.split("-")
        num1 = int(new_text_input[0])
        num2 = int(new_text_input[1])
        return num1 - num2

    elif "*" in text_input:
        new_text_input = text_input.split("*")
        num1 = int(new_text_input[0])
        num2 = int(new_text_input[1])
        return num1 * num2

    elif "/" in text_input:
        new_text_input = text_input.split("/")
        num1 = int(new_text_input[0])
        num2 = int(new_text_input[1])

        if num2 == 0:
            return "Division by 0/ZERO not allowed"
        else:
            return num1 / num2

    elif "~" in text_input:
        new_text_input = text_input.split("~")
        num1 = int(new_text_input[0])
        num2 = int(new_text_input[1])

        if num2 == 0:
            return "Division by 0/ZERO not allowed"
        else:
            return f"{num1 // num2}; The remainder is {num1 % num2}"

    else:
        return "Wrong Operator"


print("Welcome to the Python calculator!")

num_of_calculation = int(input("How many calculations do you want to do? "))

for number in range(num_of_calculation):
    user_input = input("What do you want to calculate? ")
    result = calculate(user_input)
    print(f"The answer is {result}")