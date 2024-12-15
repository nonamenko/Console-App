def calculator():
    print("=== Програмний Калькулятор ===")
    print("Оберіть операцію: +, -, *, / або 'вихід' для завершення")

    while True:
        operation = input("Введіть операцію: ").strip()
        
        if operation.lower() == "вихід":
            print("Дякуємо за використання калькулятора!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Некоректна операція. Спробуйте ще раз.")
            continue
        
        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Ділення на нуль неможливе.")
                    continue
                result = num1 / num2
            
            print(f"Результат: {result}\n")
        except ValueError:
            print("Будь ласка, введіть коректні числа.")

if __name__ == "__main__":
    calculator()
