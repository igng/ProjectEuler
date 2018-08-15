% Find the difference between the sum of the squares
% of the first one hundred natural numbers and the square of the sum.

clearvars;
close all;
clc;

v = 1:100;
(sum(v))^2 - sum(v.^2)