def judge(n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return "这不是个素数"
    return "这是个素数"
def search(n):
    list1=[]
    m=0
    if n==1:
        return f"没有小于{n}的素数"
    for x in range (2,n):
        z=0
        for y in range(2,int(x**0.5)+1):
            if x%y==0:
                z=z+1
                break
        if z==0:
            list1.append(x)
            m=m+1
    return f"{n}以内共有{m}个素数，他们是：\n{list1}"

print(judge(91))
print(search(100))