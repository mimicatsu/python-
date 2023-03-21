if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        if s[i].isalnum():
            print(True)
            break
        elif i == len(s)-1:
            print(False)
    for i in range(len(s)):
        if s[i].isalpha():
            print(True)
            break
        elif i == len(s)-1:
            print(False)
    for i in range(len(s)):
        if s[i].isdigit():
            print(True)
            break
        elif i == len(s)-1:
            print(False)
    for i in range(len(s)):
        if s[i].islower():
            print(True)
            break
        elif i == len(s)-1:
            print(False)
    for i in range(len(s)):
        if s[i].isupper():
            print(True)
            break
        elif i == len(s)-1:
            print(False)

#方法二

if __name__ == '__main__':
    s = input()
    print(any(list(map(lambda s: s.isalnum(),list(s)))))
    print(any(list(map(lambda s: s.isalpha(),list(s)))))
    print(any(list(map(lambda s: s.isdigit(),list(s)))))
    print(any(list(map(lambda s: s.islower(),list(s)))))
    print(any(list(map(lambda s: s.isupper(),list(s)))))
    