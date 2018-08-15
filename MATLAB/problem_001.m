% Find the sum of all the multiples of 3 or 5 below 1000.

clearvars;
close all;
clc;

v = 1:1000-1;
sum(v(or(mod(v,3) == 0, mod(v,5) == 0)))
