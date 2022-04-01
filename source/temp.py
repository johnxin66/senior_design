def helperFunc(sampleStr):
    temp = sampleStr.lower()
    new = ""
    for letter in temp:
        if letter.isalpha():
            new += letter
    

    n = len(new)
    for i in range(0,n//2):
        if(new[i] != new[-(i+1)]):
            return False
    return True

print(helperFunc("Top spo!"))

