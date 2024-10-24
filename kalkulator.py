a = int(input("Masukkan angka 1 : "))
b = int(input("Masukkan angka 2 : "))
operator = input("masukkan operator(+, -, *, /, **, //, %) : ")

if operator == '+':
    print("a + b = ", a + b)
elif operator == '-' :
    print("a - b = ", a - b)
elif operator == '*':
    print("a * b = ", a * b)
elif operator == '/':
    print("a / b = ", a / b) 
elif operator == '**' :
    print("a ** b = ", a ** b)
elif operator == '//' :
    print("a // b = ", a // b)
elif operator == '%' :
    print("a % b = ", a % b)