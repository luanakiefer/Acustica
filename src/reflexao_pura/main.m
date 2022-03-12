close all
clear all
clc

tipo_condicao_contorno = 2;
tipo_fonte = 2;
frequencia_onda = 80; % Hz

atraso_onda = 1/frequenciaOndaHertz; % s

compressibilidade_1 = 2.25*10^9;    %!modulo de compressibilidade da agua (kg/m/s^2)
compressibilidade_2 = 3.90*10^10;   %!modulo de compressibilidade da rocha (kg/m/s^2) == ( 0.39x10^12 dyn/cm^2)
compressibilidade_onda_minima = min(compressibilidade_1/compressibilidade_2, compressibilidade_2/compressibilidade_1);

ALFA = 10;
BETA = 4;

velocidade_onda_1 = 4000; % m/s
velocidade_onda_2 = 2000; % m/s
velocidade_onda_maxima = max(velocidade_onda_1, velocidade_onda_2);

comprimento_onda_1 = velocidade_onda_1/frequencia_onda; % m
comprimento_onda_2 = velocidade_onda_2/frequencia_onda; % m
comprimento_onda = min(comprimento_onda_1, comprimento_onda_2); % m

comprimento_dominio_x = 1100; % m
espacamento_grade_x = 1; % m

comprimento_dominio_y = 600; % m
espacamento_grade_y = espacamento_grade_x; % m

delta_s = sqrt(espacamento_grade_x ^ 2 + espacamento_grade_y ^ 2);

eixo_x = 0:espacamento_grade_x:comprimento_dominio_x;
eixo_y = 0:espacamento_grade_y:comprimento_dominio_y;

nx = length(eixo_x);
ny = length(eixo_y);

% Grade
[X, Y] = meshgrid (eixo_x, eixo_y);

posicao_fonte_x = 2;
posicao_fonte_y = 550;

% Campo de velocidades
velocidade_onda = zeros(ny,nx);

% INCLUIR SIMULAÇÕES

matriz_compressibilidades = zeros(ny,nx);
matriz_compressibilidades(:,:) = compressibilidade_1;
matriz_compressibilidades(1:250,:) = compressibilidade_2;

Cr=1; % --

delta_tempo_1 = 1/frequencia_onda/60; % min
delta_tempo_2 = espacamento_grade_x/(BETA * max(velocidade_onda(:)));
delta_tempo_3 = Cr * (espacamento_grade_x * espacamento_grade_y) / (delta_s * velocidade_onda_maxima);
delta_tempo = min([delta_tempo_1, delta_tempo_2, delta_tempo_3]);

tempo_final_simulacao=0.5; % s

passo_tempo = floor(tempo_final_simulacao/delta_tempo);
passo_arquivamento = 10;

%plot(t,fonte(LT,t))

het2(
    espacamento_grade_x,
    delta_tempo,
    uint64(passo_tempo),
    uint64(nx),
    uint64(ny),
    uint64(posicao_fonte_x),
    uint64(posicao_fonte_y),
    atraso_onda,
    frequencia_onda,
    velocidade_onda,
    uint64(passo_arquivamento),
    uint64(tipo_condicao_contorno),
    uint64(tipo_fonte),
    matriz_compressibilidades);
%for i=parq:parq:N
% p=load(strcat('resufados/p',num2str(i),'.mat'));
% contourf(X,Y,p)
% title(strcat('t=',num2str(i*dt)))
%  pause(dt)
% endfor