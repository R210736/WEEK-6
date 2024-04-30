import matplotlib.pyplot as plt
x=[7,2,8,9,5]
y=[8,9,8,5,8]
lx=len(x)
ly=len(y)
ki=[]
z={}
sum=[]
for k in range(0,lx):
    summation=0
    for n in range(len(x)):
        if n+k<len(y):
            summation+=x[n]+y[n+k]
    sum.append(k)
    ki.append(k)
    z[k]=summation
print(z)
plt.plot(z,ki)
plt.show()