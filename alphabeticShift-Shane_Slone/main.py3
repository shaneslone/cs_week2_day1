def alphabeticShift(inputString):
    output = ""
    for i in range(len(inputString)):
        if inputString[i] == "z":
            output += "a"
        else:
            value = ord(inputString[i])
            output += chr(value + 1)
    return output

