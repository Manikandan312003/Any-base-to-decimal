def convertToDecimal(number,base):
    converted,current=0,1
    while number:
        converted+=number%10*current
        current*=base
        number//=10
    return converted

print(convertToDecimal(1010,2))
print(convertToDecimal(22,3))