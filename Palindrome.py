iNum = int(input("Enter a number"))
iReverse = 0
iFrequency = {}
iTemp = iNum

while iTemp > 0:
    iDigit = iTemp % 10
    iReverse = (iReverse * 10) + iDigit
    iTemp = iTemp // 10
    if iDigit in iFrequency:
        iFrequency[iDigit] += 1
    else:
        iFrequency[iDigit] = 1

if iReverse == iNum:
    print("Palindrome")
else:
    print("Not Palindrome")

for key, value in iFrequency.items():
    print(key, ":", value)