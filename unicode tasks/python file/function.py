n1=int(input("Enter any decimal number: "))
n2=int(input("Enter any decimal number: "))

    
p={}
t={}
for number in range(n1,n2+1):
   
    x=bin(number)
    
    p[number]=x
    new="11"
    if new in x:
        t[number]="true"
    else :
        t[number]="false"
  
print(p)
print(t)

# driver code 
 



