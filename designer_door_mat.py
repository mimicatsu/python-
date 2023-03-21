import math

def door(N,M):
    half_hight = math.ceil(N)
    pattern = '.|.'
    for i in range(1,half_hight,2):
        print((i*pattern).center(M,'-'))
       
    welcome = 'WELCOME'
    print(welcome.center(M,'-'))
    
    for i in range(half_hight-2,0,-2):
        print((i*pattern).center(M,'-'))
  
        
    return


N,M = map(int, input().split())
door(N,M)
