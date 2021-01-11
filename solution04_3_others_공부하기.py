# 1 1.70s
def ispalindrome(string):
    decide = 1
    i = 0
    while i <= int(len(string) / 2) and decide == 1:
        if string[i] != string[-(i + 1)]:
            decide = 0
        i += 1
    return decide

aux = 0
for k in range(101, 1000):
    for j in range(101, 1000):
        if ispalindrome(str(j * k)) and j * k > aux:
            aux = j * k
print(aux)

# 2 0.85s
def IsPalindrome(n):
    myStr = str(n)
	if myStr == myStr[::-1]:
		return 1
	else:
		return 0
import time

tStart = time.time()
nResult = 0
for i in range(100,1000):
    for j in range(100,1000):
        if IsPalindrome(i*j) == 1 and (i*j) > nResult:
            nResult = (i*j)
print ("Winner = " + str(nResult))
print ("run time = " + str((time.time() - tStart)))