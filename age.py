a={}
b=int(input())
i=0
while i<b:
   no=int(input())
   name=input()
   age=int(input())
   hair_color=input()
   eyes=input()
   a[no]={}
   a[no][name]={}
   a[no][name]["age"]=age
   a[no][name]["hair_color"]=hair_color
   a[no][name]["eye_color"]=eyes
   i+=1
print(a)   
