a = eval(input("Enter the value a: " ))
b = eval(input("Enter the value b: " ))

print(
    ("\n"),
    "Important Note:- Spelling Mistakes Will Rasie An Error!",("\n"),("\n"),
    "Type add For Addition",("\n"),
    "Type sub For Subition",("\n"),
    "Type mul For Multiplication",("\n"),
    "Type div For Division",("\n")
)

operation = input("Enter Required Operatio: " )

if operation == "add":
    ans = a+b
    print("Answer is: ",ans)
elif operation == "sub":
    ans = a-b
    print("Answer is: ",ans)
elif operation == "mul":
    ans = a*b
    print("Answer is: ",ans)
elif operation == "div":
    ans = a/b
    print("Answer is: ",ans)
else: 
    print("Please Check The Spelling")
    raise ValueError("Invalid Operation")
