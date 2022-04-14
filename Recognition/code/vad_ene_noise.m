clear

[x,fs] = audioread('v:\bat\sounds\tst_male_english-original.wav');
x = x(360000+(1:2*fs));
N = length(x);

y = filter(1,[1 -.68],randn(length(x),1));
y = y*norm(x)/norm(y);

u = x+y;
u = u*norm(x)/norm(u);

audiowrite('vad_orig.wav',x,fs)
audiowrite('vad_noisy.wav',y,fs)
audiowrite('vad_noise.wav',u,fs)


winlen = 320;
winstep = winlen/2;


for q=[3 4]

thresh = [15 q];

wincnt = 1+floor((length(x)-winlen)/winstep);

ene = zeros(wincnt,2);
for k=1:wincnt
    ene(k,1) = norm(x((k-1)*winstep + (1:winlen)).*hamming(winlen));
    ene(k,2) = norm(u((k-1)*winstep + (1:winlen)).*hamming(winlen));
end
ene(:,2) = ene(:,2)*max(ene(:,1))/max(ene(:,2));
tre(:,1) = sign(10*log10(ene(:,1))+thresh(1));
tre(:,2) = sign(10*log10(ene(:,2))+thresh(2));

clf
subplot(311)
plot((1:N)/fs,[x y-.4 u-.7])
axis([0 N/fs -1 .2])
title('Input speech signal, noise and noisy speech (SNR 0dB)')
ylabel('Amplitude')
legend('Speech','Noise','Noisy speech','Location','East')
set(gca,'YTick',[])

subplot(312)
plot((1:wincnt)*N/(wincnt*fs),10*log10(ene))
hold on
plot([0 N/fs],-thresh(1)*[1 1],'--b') 
plot([0 N/fs],-thresh(2)*[1 1],'--r') 
axis([0 N/fs -40 5])
title('Framewise energy')
ylabel('Magnitude (dB)')
legend('Clean','Noisy','Clean threshold','Noisy threshold','Location','Southeast')

subplot(313)
plot((1:wincnt)*N/(wincnt*fs),[tre(:,1)+.05 tre(:,2)-.05])
hold on
axis([0 N/fs -2.2 2.2])
title('VAD decision')
xlabel('Time (s)')
set(gca,'YTick',[-2 -1.5 -1 1 1.5 2 ],'YTicklabel',{'true negative','false negative','non-speech','speech','false positive','true positive'})
legend('Clean','Noisy','Location','East')

ix = find((tre(:,1) == 1) & (tre(:,2) == 1));
plot(ix*N/(wincnt*fs),0*ix + 2,'kx')
ix = find((tre(:,1) ~= 1) & (tre(:,2) == 1));
plot(ix*N/(wincnt*fs),0*ix + 1.5,'ro')
ix = find((tre(:,1) ~= 1) & (tre(:,2) ~= 1));
plot(ix*N/(wincnt*fs),0*ix - 2,'kx')
ix = find((tre(:,1) == 1) & (tre(:,2) ~= 1));
plot(ix*N/(wincnt*fs),0*ix - 1.5,'ro')

print(['vad_ene_noise' num2str(q) '.eps'], '-deps2c')

end