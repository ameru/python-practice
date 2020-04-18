def problem_1()-> None:
    input_1 = int(input("Enter a number between 1-20: "))
    print(int((((input_1 * 2) + 10) / 2) - input_1))


def problem_2()-> None:
    input_1 = int(input("Enter a number: "))
    input_2 = int(input("Enter a number: "))
    input_3 = input_1 + input_2
    input_4 = input_2 + input_3
    input_5 = input_3 + input_4
    input_6 = input_4 + input_5
    input_7 = input_5 + input_6
    input_8 = input_6 + input_7
    input_9 = input_7 + input_8
    input_10 = input_8 + input_9
    print(int((input_1 + input_2 + input_3 + input_4 + input_5 + 
        input_6 + input_7 + input_8 + input_9 + input_10) / input_7))


def problem_3()-> None:
    input_1 = int(input("Enter a four-digit number, each digit different: "))
    first_digit = input_1 // 1000
    second_digit = (input_1 // 100) % 10
    third_digit = (input_1 // 10) % 10
    fourth_digit = (input_1 % 1000) % 10
    result = (fourth_digit * 1000) + (second_digit * 100) + (third_digit * 10) + first_digit
    diff = max(input_1, result) - min(input_1, result)
    first_digit = diff // 1000
    second_digit = (diff // 100) % 10
    third_digit = (diff // 10) % 10
    fourth_digit = (diff % 1000) % 10
    result2 = first_digit + second_digit + third_digit + fourth_digit
    first_digit = result2 // 10
    second_digit = result2 % 10
    print(int(first_digit + second_digit))

def problem_4()-> None:
    input_1 = int(input("Enter a number 1-50, not div by 7: "))
    result = input_1 / 7
    result2 = result % 1
    first_digit = result2 // 0.1
    second_digit = (result2 // 0.01) % 10
    third_digit = (result2 // 0.001) % 10
    fourth_digit = (result2 // 0.0001) % 10
    fifth_digit = (result2 // 0.00001) % 10
    sixth_digit = (result2 // 0.000001) % 10
    print(int((first_digit + second_digit + third_digit + fourth_digit + fifth_digit + sixth_digit)))


if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
