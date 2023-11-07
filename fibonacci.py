def fib(iNum):
    if iNum <= 0:
        return "Error"
    elif iNum == 1:
        return 0
    elif iNum == 2:
        return 0, 1
    else:
        iFibonacci = [0, 1]
        i = 2
        while i <= iNum - 1:
            iNextValue = iFibonacci[-1] + iFibonacci[-2]
            iFibonacci.append(iNextValue)
            i = i + 1
        return iFibonacci


iNum = int(input("Enter the Number"))
print(fib(iNum))
