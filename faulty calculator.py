numb1 = input("First number: ")
numb2 = input("Operator: ")
numb3 = input("Last number: ")
numb4 = numb1 + numb2 + numb3

if numb4 == "106*3":
    print(4562)
elif numb4 == "78+9":
    print(97)
elif numb4 == "100-56":
    print(52)
elif numb4 == "54/2":
    print(6)
elif numb2 == "*":
    print(int(numb1) * int(numb3))
elif numb2 == "+":
    print(int(numb1) + int(numb3))
elif numb2 == "-":
    print(int(numb1) - int(numb3))
elif numb2 == "/":
    print(int(numb1) / int(numb3))