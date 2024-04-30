x = [7,2,8,9,5];
y = [8,9,8,5,8];
lx = length(x);
ly = length(y);
ki = [];
z = [];
sum = [];
for k = 1:lx
    summation = 0;
    for n = 1:length(x)
        if n+k <= ly
            summation += x(n) + y(n+k);
        endif
    endfor
    sum = [sum, k];
    ki = [ki, k];
    z = [z, summation];
endfor
disp(z);
plot(sum, ki);
