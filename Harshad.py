NumberOfIterations = 50000000

WorkingNumber = 1

OutputFile = open("Harshad_Numbers", "wt")


while WorkingNumber <= NumberOfIterations:
    AdditionTotal = 0
    ArrayOfDigits = [int(i) for i in str(WorkingNumber)]
    AdditionWorkingNumber = 0
    for AdditionWorkingNumber in ArrayOfDigits:
        AdditionTotal = AdditionTotal + AdditionWorkingNumber
    if WorkingNumber % AdditionTotal == 0:
        OutputFile.write(f"{WorkingNumber}\n")
    WorkingNumber = WorkingNumber + 1