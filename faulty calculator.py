# Faulty Calculator Program
# 56+9=77
# 45*3=555
# 56/6=4
val1 = float(input("Enter your first  number: "))
val2 = float(input("Enter your second number: "))
op = input("Enter a operator \n + \n - \n * \n %\n ")
if op == "+":
    print("Addition is =", val1+val2)

elif op == "-":
    print("Subtaction is =", val1-val2)
elif op == "*":
    print("Multiplication is =", val1*val2)
elif op == "%":
    print("Division is =", val1/val2)
else:
    print("Error Please give a right operator")
