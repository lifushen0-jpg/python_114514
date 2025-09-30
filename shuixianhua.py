def shuixianhua():
    list1=[]
    for x in range(1,10):
        for y in range(0,10):
            for z in range(0,10):
                n=x*100+y*10+z
                if n==x*x*x+y*y*y+z*z*z:
                    list1.append(n)
    m=len(list1)
    print(f"水仙花数有{list1},共{m}个")
shuixianhua()