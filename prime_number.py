#1
def solution(n):
    answer=0
    number=[]
    s_number=[]
    for i in range(n+1):
        number.append(i)
    for i in range(2,n+1,1):
        if i==-1:
            continue
        j=0
        for j in range(i+i,n+1,i):
            number[j]=-1
    for i in range(2,n+1):
        if number[i]!=-1:
            s_number.append(i)
    return s_number

print(solution(73))

#2
def is_prime(n):
    a=0
    for i in range(2,n) :
        if n%i==0:
            a+=1
    if a==0:
        print("{}는 소수이다.".format(n))
    else:
        print("{}는 소수가 아니다.".format(n))

is_prime(31)
