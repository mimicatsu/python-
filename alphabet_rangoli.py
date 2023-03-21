import math

def print_rangoli(size):
    half_size = math.ceil(size/2)
    lst = [] 
    lst_under = []
    
    for i in range(size-1,-1,-1):
        alpha = chr(i+97)
        ctr = "-".join(''.join(lst)+alpha+''.join(lst[::-1]))
        line = (ctr).center(2*size+2*(size-1)-1,'-')
        print(line)
        lst_under.append(line)
        lst.append(alpha)
     
    for j in range(size-2,-1,-1):
        print(lst_under[j])
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)