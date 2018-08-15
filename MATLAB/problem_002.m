% By considering the terms in the Fibonacci sequence whose values
% do not exceed four million, find the sum of the even-valued terms.

clearvars;
close all;
clc;

% fibonacci(33) = 3524578
% fibonacci(34) = 5702887

f = fibonacci(2:33);
sum(f(mod(f,2) == 0))