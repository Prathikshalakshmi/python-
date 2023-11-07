def binToDec(iBinary):
    iDecimal = 0
    iPower = 0
    while iBinary != 0:
        iDigit = iBinary % 10
        iDecimal += iDigit * (2 ** iPower)
        iBinary //= 10
        iPower += 1
    return iDecimal


def octToHexadec(iOctal):
    iDecimal = 0
    iPower = 0
    while iOctal != 0:
        iDigit = iOctal % 10
        iDecimal += iDigit * (8 ** iPower)
        iOctal //= 10
        iPower += 1

    iHexadecimal = ""
    while iDecimal != 0:
        iRemainder = iDecimal % 16
        if iRemainder < 10:
            iHexadecimal = str(iRemainder) + iHexadecimal
        else:
            iHexadecimal = chr(ord('A') + iRemainder - 10) + iHexadecimal
        iDecimal //= 16

    return iHexadecimal


# Binary to Decimal conversion
iBinaryNum = input("Enter a binary number: ")
iDecimalNum = binToDec(int(iBinaryNum))
print("Decimal: ", iDecimalNum)

# Octal to Hexadecimal conversion
iOctalNum = input("Enter an octal number: ")
iHexadecimalNum = octToHexadec(int(iOctalNum))
print("Hexadecimal: ", iHexadecimalNum)
