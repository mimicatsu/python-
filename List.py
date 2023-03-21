if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for i in range(N):
        lst = list(input().split())
        if lst[0] == 'insert':
            arr.insert(int(lst[1]),int(lst[2]))
        if lst[0] == 'print':
            print(arr)
        if lst[0] == 'remove':
            arr.remove(int(lst[1]))
        if lst[0] =='append':
            arr.append(int(lst[1]))
        if lst[0] == 'sort':
            arr.sort()
        if lst[0] == 'pop':
            arr.pop()
        if lst[0] == 'reverse':
            arr.reverse()
            
        
  