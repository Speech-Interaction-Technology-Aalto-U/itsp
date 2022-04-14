clear

[x,fs] = audioread('v:\bat\sounds\tst_male_english-original.wav');
x = x(360000+(1:2*fs));
N = length(x);

u = filter(1,[1 -.68],randn(length(x),1));
u = u*norm(x)/norm(u);

y = x+.01*u;
y = y*norm(x)/norm(y);

thresh = 15;

winlen = 320;
winstep = winlen/2;
hwin = hamming(winlen);
wincnt = 1+floor((length(x)-winlen)/winstep);
M = 2^12;
S = round(.5*(M/winlen)*fs./[450 80]);



% feature calculation
ene = zeros(wincnt,2);
for k=1:wincnt
    xwin = x((k-1)*winstep + (1:winlen)).*hwin;
    ywin = y((k-1)*winstep + (1:winlen)).*hwin;
    ene(k,1) = norm(xwin);
    ene(k,2) = norm(ywin);
    
    rx = xcorr(xwin,1);
    ry = xcorr(ywin,1);
    r2(k,:) = [rx(1)/rx(2) ry(1)/ry(2)];
    
    % F0/cepstrum
    X = abs(fft(20*log10(abs(fft(xwin,M))+eps)));
    [~,tx] = max(X(S(1):S(2))); tx = tx+S(1)-1;
    Y = abs(fft(20*log10(abs(fft(ywin,M))+eps)));
    [~,ty] = max(Y(S(1):S(2))); ty = ty+S(1)-1;
    
    T(k,:) = [tx ty];
    G(k,:) = [X(tx)/X(1) Y(ty)/Y(1)];
    
    if 0
        clf
        subplot(211)
        plot([xwin ywin])
        subplot(212)
        semilogy([X Y])
        hold on
        semilogy([tx ty],[X(tx) Y(ty)],'x')
        semilogy(S,[1 1])
        waitforbuttonpress
    end
    
end

F1 = [ene(:,1) r2(:,1) T(:,1) G(:,1)];
F2 = [ene(:,2) r2(:,2) T(:,2) G(:,2)];
for k=1:4
    F1(:,k+4) = filter([1 -1],1,F1(:,k));
    F2(:,k+4) = filter([1 -1],1,F2(:,k));
    F1(:,k+8) = filter([1 -2 1],1,F1(:,k));
    F2(:,k+8) = filter([1 -2 1],1,F2(:,k));
end
for k=1:12
    F1(:,k) = F1(:,k)-mean(F1(:,k));
    F2(:,k) = F2(:,k)-mean(F2(:,k));
    F1(:,k) = F1(:,k)/std(F1(:,k));
    F2(:,k) = F2(:,k)/std(F2(:,k));
end
F1(:,3+[4 8]) = abs(F1(:,3+[4 8]));
F2(:,3+[4 8]) = abs(F2(:,3+[4 8]));

[V1,D1] = eig(F1'*F1);
[V2,D2] = eig(F2'*F2);
W1 = F1*V1*sqrt(inv(D1));
W2 = F2*V2*sqrt(inv(D2));


target = sign(10*log10(ene(:,1))+thresh);
ix = find(target == 1); target(1+ix(1:end-1)) = 1;


a = inv(W2'*W2)*W2'*target;

noisy_output = W2*a;
noisy_output(1:3) = 0;
noisy_output(:,2) = sign(noisy_output-.2);
noisy_output(:,3) = noisy_output(:,2);
ix = find(noisy_output(:,3) > 0);
for k=[-1 1:3]
    noisy_output(ix(1:end-max(k,0))+k,3) = 1;
end

clf
subplot(511)
plot(x)
axis tight
title('Speech signal')
set(gca,'YTick',[],'Xtick',[])

subplot(512)
plot(ene)
axis tight
title('Signal energy')
set(gca,'Xtick',[])

subplot(513)
plot(r2)
axis tight
title('Signal correlation r_1/r_0')
set(gca,'Xtick',[])

subplot(514)
plot(T)
axis tight
title('Fundamental frequency F_0')
set(gca,'Xtick',[])

subplot(515)
plot(G)
axis tight
title('Cepstral peak size C_{max}/C_0')
xlabel('Time (frame)') 

print -deps2c vad_features1.eps



clf
subplot(511)
plot(x)
axis tight
title('Speech signal')
set(gca,'YTick',[],'Xtick',[])

subplot(512)
plot(diff(ene))
axis tight
title('Signal \Delta-energy')
set(gca,'Xtick',[])

subplot(513)
plot(diff(r2))
axis tight
title('Signal \Delta-correlation r_1/r_0')
set(gca,'Xtick',[])

subplot(514)
plot(diff(T))
axis tight
title('\Delta-Fundamental frequency F_0')
set(gca,'Xtick',[])

subplot(515)
plot(diff(G))
axis tight
title('\Delta-Cepstral peak size C_{max}/C_0')
xlabel('Time (frame)') 


print -deps2c vad_features2.eps




clf
plot((1:N)/fs, x/std(x))
hold on

plot((1:wincnt)*winstep/(fs),target+3)

strs{13} = 'Speech';
strs{14} = 'Target output';
for k=1:12
    plot((1:wincnt)*winstep/(fs),F1(:,k)-k*3)
    strs{13-k} = ['Feature ' num2str(k)];
end
axis([0 2 -38 5])
set(gca,'YTick',fliplr((-1:12)*-3),'YTickLabel',strs)
title('(Features - mean)/standard deviation')

print -deps2c vad_features3.eps


clf
plot((1:N)/fs, x/std(x))
hold on

plot((1:wincnt)*winstep/(fs),target+3)

strs{13} = 'Speech';
strs{14} = 'Target output';
for k=1:12
    plot((1:wincnt)*winstep/(fs),W1(:,k)/std(W1(:,k))-k*3)
    strs{13-k} = ['Feature ' num2str(k)];
end
axis([0 2 -38 5])
set(gca,'YTick',fliplr((-1:12)*-3),'YTickLabel',strs)
title('Whitened features')

print -deps2c vad_features4.eps



clf
plot((1:N)/fs, .6*x/std(x)+.5)
hold on

plot((1:wincnt)*winstep/(fs),target+3)
plot((1:wincnt)*winstep/(fs),noisy_output(:,1)+5)
plot((1:wincnt)*winstep/(fs),noisy_output(:,2)+7)
plot((1:wincnt)*winstep/(fs),noisy_output(:,3)+8)

set(gca,'YTick',[.5 3 5.5 7 8],'YTickLabel',{'speech','target','output','output+trehshold','output+hangover'})
axis([0 2 -3 9.5])
title('Linear classifier VAD on noisy speech')

print -deps2c vad_features5.eps
