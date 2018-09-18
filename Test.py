print("a(n)=a(n-1)*k+b")
print("Dieses Programm soll b berechnen. Es benötigt zunäcsht einige Werte...")
a=[]
a.append(int(input("a(0)=")))
k = float(input("k="))
n= int(input("n="))

b=-14000
i=0
while(i<=n):
    a.append(0)
    i+=1


f:
i=0
#print("Here I am")
while(i<=n):
    #print("in loop")
    i+=1
    #print("1")
    a[i] = (a[i-1]*k)+b
    #print("Test")

print("a[" + str(n) + "]=" + str(a[n]))
