# factors.py

n = input("Give me a number: ")
n = int(n)
factors = []

if n % 2 == 0:
    half = int(n / 2)
else:
    half = int((n-1) / 2)

for i in range(1, half+1) :
    if n % i == 0:
        print(i)
        factors.append(i)
factors.append(n)
print('Final result:')
for j in factors:
    if j != n:
        print('{}, '.format(j), end='')
    else:
        print('{}'.format(j))

