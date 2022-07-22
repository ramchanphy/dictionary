# l=[1,2,3,4]
# l1={n:n for n in l }
# print(l1)
# d={}
# i=1
# while i<len(l):
#     d[i]=i
#     i+=1
# print(d)



# dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# for i in dic:
#     for j in dic[i]:
#         k=j
#     dic[i]=k
# print([dic])
# l=[]
# d={}
# for i,j in dic.items():
#     for k in j:
#         d={i:k}
#     l.append(d)
# i=0
# while i<len(l):
#     d.update(l[i])
#     i+=1
# print([d])

   
    
    


# dic={'x': '10', 'y': '20', 'z': '30','p': '40', 'q': '50', 'r': '60'}
# d={}
# for i in dic:
#     for j in dic:
#         k=j
#         # d[i]=k
# print(k)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# a={**dic1,**dic2,**dic3}
# print(a)

# from tkinter import E


# user=int(input())
# b=[]
# i=1
# while i<=user:
#     a=[]
#     j=1
#     e=i
#     s=0
#     while j<=user:
#         s+=e
#         a.append(s)
#         j+=1
#     b.append(a)
#     i+=1
# print(b)
# user=input()
# if len(user)==4 or len(user)==6:
#     a=[]
#     i=0
#     while i<len(user):
#         if user[i].isdigit():
#             a.append(user[i])
#         i+=1
#     if len(a)==len(user):
#         print(True)
#     else:
#         print(False)
        
# d={"grace":[20,40,60],"chanphy":[20,30,70],"semi":[40,20,68]}
# for i in d:
#     sum=0
#     c=0
#     for j in d[i]:
#         c+=1
#         sum+=j
#     a=sum/c
#     print(a)
# d={1:"10",2:"20",3:"30",4:"40"}
# dict={}
# for i in d:
#     for j in d[i]:
#         if d[i] .isdigit():
#             a=int(d[i])
#             dict[i]=a
# print(dict)
# dic=[{"x":"10","y":"20"},{"p":"30","q":"40"}]
# d={}
# print(len(dic))
# i=0
# while i<len(dic):
#     j=0
#     while j <len(dic[i]):
#         if j.isdigit():
#             a=int(j)
#             d[i]=a
#         j+=1
#     i+=1
# print(d)
# for i in dic:
#     for j in dic[i]:
#         if j.isdigit():
#             a=int(dic[i])
#             d[i]=a
# print(d)
n=int(input())
while n>0:
    n1,n2,n3=map(int,input().split())
    if n1>n2 and n1>n3:
        if n2>n3:
            print(n2)
        else:
            print(n3)
    elif n2>n3 and n2>n1:
        if n3>n1:
            print(n3)
        else:
            print(n1)
    else:
        if n1>n2:
            print(n1)
        else:
            print(n2)
    n-=1 