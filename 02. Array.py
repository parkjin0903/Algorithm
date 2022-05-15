from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__=='__main__':
    print('maximum of the array')
    num = int(input('put number of elements'))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'put x[{i}]: '))
        
    print(f'maximum is {max_of(x)}.')