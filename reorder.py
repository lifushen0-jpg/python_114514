def ascending_order(list1):
    if type(list1)!=list:
        return "请输入列表"
    n=len(list1)
    list2=[]
    while len(list2)<n:
        j=list1[0]
        for i in list1:
            if i>j:
                j=i
        list2.append(j)
        list1.remove(j)
    return list2
def descending_order(list1):
    if type(list1)!=list:
        return "请输入列表"
    n=len(list1)
    list2=[]
    while len(list2)<n:
        j=list1[0]
        for i in list1:
            if i<j:
                j=i
        list2.append(j)
        list1.remove(j)
    return list2
def maximum(list1):
    if type(list1)!=list:
        return "请输入列表"
    j=list1[0]
    for i in list1:
        if i>j:
            j=i
    return j
def minimum(list1):
    if type(list1)!=list:
        return "请输入列表"
    j=list1[0]
    for i in list1:
        if i<j:
            j=i
    return j