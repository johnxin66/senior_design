def helperFunc(sampleStr):
    n = len(sampleStr)
    for i in range(0,n/2):
        if(sampleStr[i] != sampleStr[-(i+1)]):
            return False
    return True

print(helperFunc("mom"))