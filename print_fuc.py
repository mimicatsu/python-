if __name__ == '__main__':
    n = int(input())
    list = []
    for i in range(n):
        list.append(i+1)
    string = "".join(map(str,list))
    print(string)
        