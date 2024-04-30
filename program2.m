x=[]
lx=input("Enter x array length:")
h=0
for i=1:lx
  l=input("Enter lx:");
  x=[x,l];
 endfor
 ly=input("enter ly");
 t=0:0.01:ly
 for i=1:lx
   h+=x(i)*cos(2*pi*t*i)
 endfor
plot(h)