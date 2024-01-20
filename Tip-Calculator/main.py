print("Welcome to the Tip Calculator")
bill = float(input("What is your bill? $"))
tip = int(input("How much tip would u give? 10, 12, 15? %"))
people = int(input("Among how many would u split the bill?"))
total_bill = bill + (bill*tip)/100
div = total_bill/people
ind = round(div)
print(f"Each person should pay: {ind}")