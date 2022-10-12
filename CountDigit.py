
# input1 = input()
numberInput = int(input())
numberBase = int(input())

i = 0
result = numberInput

while result > 1:
    result = numberInput/numberBase**i
    i += 1
print(i - 1)




