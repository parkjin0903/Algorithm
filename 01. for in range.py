print('print *')
n = int(input('how many stars?'))
w= int(input('new line'))

for _ in range(n//w):
    print('*'*w)
    
rest = n % w
if rest:
    print('*'* rest)
    
print(n//w)