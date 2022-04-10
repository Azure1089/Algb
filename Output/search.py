a = ["3","5","9","6","58","36","28","71","987","65","apple","banana","blue","damian"]
def linear_search(search,a):
    found = 0
    for i in range(len(a)):
        if a[i-1] == search:
            found = 1
            return i
    if found == 0:
        return 'That item wasn\'t in the list or was misspelt'
def binary_search(search_term,a):
    a_i=[]
    b_i = []
    c_i = []
    found = 0
    for i in range(len(a)):
        a_i.append(i)
    while found != 1:
        midpoint_i = int(a_i[(int(len(a_i))//2)])
        midpoint = int(a[midpoint_i])
        if search_term == midpoint:
            return midpoint_i+1
        elif search_term < midpoint:
            b_i = []
            for i in range((int(len(a_i))//2)):
                b_i.append(a_i[i])
            a_i = []
            for i in range(len(b_i)):
                a_i.append(b_i[i])
        
        else:
            b_i = []
            for i in range((int(len(a_i))//2)):
                b_i.append(a_i[-(i+1)])
            for i in range(len(b_i)):
                c_i.append(b_i[-(i+1)])
            b_i = []
            for i in range(len(c_i)):
                b_i.append(c_i[i])
            a_i = []
            for i in range(len(b_i)):
                a_i.append(b_i[i])