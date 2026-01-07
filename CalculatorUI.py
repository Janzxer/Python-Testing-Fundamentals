import CalculatorUtils
# aloitetaan looppi luomalla muuttuja operand ja sille arvo
operand = "start"
# niin kauan kun operandin value on MUUTA kuin exit, loopataan.
while operand != "exit":
    # kysytään käyttäjältä arvo operandille, jonka pohjalta toimitaan.
    operand = input("Do you want to +, -, * or / ? Type 'exit' to stop ")

    if operand != "exit":
        number1 = int(input("Give me the first number: "))
        number2 = int(input("Give me the second number: "))

        # matchillä katotaan mitä käyttäjä on laittanut
        match operand:
            case "+":
                print(CalculatorUtils.addition(number1,number2))
            case "-":
                print(CalculatorUtils.subtraction(number1,number2))
            case "*":    
                print(CalculatorUtils.multiplication(number1,number2))
            case "/":    
                print(CalculatorUtils.division(number1,number2))
    else:
        print("Thank you come again!")
