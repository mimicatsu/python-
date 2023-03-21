if __name__ == '__main__':
    lst_st = []#姓名+分數
    lst_score = []#分數
    lst_name = []#姓名
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst_score.append(score)
        lst = []
        lst.append(name)
        lst.append(score)
        lst_st.append(lst)
    
#找出第二小的分數   
    min_score = 100
    mid_score = 100
    for i in range(len(lst_score)):
        if lst_score[i] < min_score:
            mid_score = min_score
            min_score = lst_score[i]
        elif lst_score[i] > min_score and lst_score[i] < mid_score:
            mid_score = lst_score[i]
    
#找出第二小分數的學生           
    for i in range(len(lst_st)):
        if lst_st[i][1] == mid_score:
            lst_name.append(lst_st[i][0])
#將學生用姓名排序    
    lst_name = sorted(lst_name)
    for i in range(len(lst_name)):
        print(lst_name[i])      
 