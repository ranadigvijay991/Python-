x=int(input("upto which no:"))
i=1
n1=0
n2=1
print(n1,"\t",n2,end="")
while(i<=x ):
    n3=n1+n2
    n1=n2
    n2=n3
    i=i+1
    if(n3<=x):
        print("\t",n3,"\t",end="")

