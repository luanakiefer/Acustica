%M1
cw(:,:)=4000;
cw(1:250,:)=2000;

%M2
##cw(1:100,:)=2000;
##cw(101:200,:)=2500;
##cw(201:300,:)=3000;
##cw(301:400,:)=3250;
##cw(401:500,:)=3500;
##cw(501:600,:)=4000;

%M3
##cw(1:200,1:300) = 2000;
##cw(1:200,301:700) = 2250;
##cw(1:200,701:1101) = 2500;
##cw(201:400,1:300) = 2750;
##cw(201:400,301:700) = 3000;
##cw(201:400,701:1101) = 3250;
##cw(401:601,1:300) = 3500;
##cw(401:601,301:700) = 3750;
##cw(401:601,701:1101) = 4000;

%M4
##cw=zeros(ny,nx);
##cw(:,:)=4000;
##cw(1:115,:)=2000;
##cw(116:231,:)=2500;
##cw(232:324,:)=3000;
##cw(171:286,400:690)=4000;

%M5
##for i=1:nx
##  for j=1:ny
##    if(y(j)<=200 || (x(i)>=550 && y(j)<=300))
##      cw(j,i) = 2000;
##    elseif((x(i)<=450 && y(j)<=400) || (x(i)>=450 && y(j)<=400 && y(j)>=300) || (x(i)>= 750 && y(j)>=400 && y(j)<=500))
##      cw(j,i) = 3000;
##    elseif((x(i)<=650 && y(j)>=400) || y(j)>=500)
##      cw(j,i) = 4000;
##    endif
##    
##    if(y(j)>=200 && y(j)<=300 && x(i)>=450 && x(i)<=550)
##      if(x(i)-450>=y(j)-200)
##        cw(j,i)=2000;
##      else
##        cw(j,i)=3000;
##      endif
##    endif
##    
##    if(y(j)>=400 && y(j)<=500 && x(i)>=650 && x(i)<=750)
##      if(x(i)-650>=y(j)-400)
##        cw(j,i)=3000;
##      else
##        cw(j,i)=4000;
##      endif
##    endif
##    
##  endfor
##endfor

%M6
##cw(:,:) = 4000;
##cw(1:114,:) = 2000;
##cw(115:207,174:928) = 2000;
##cw(115:138,116:986) = 2000;
##cw(208:264,232:870) = 3000;
##cw(265:334,290:812) = 3000;
##cw(335:381,348:754) = 3000;
##cw(382:405,406:696) = 3000;