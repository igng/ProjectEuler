% Find the largest palindrome made from the product of two 3-digit numbers.

clearvars;
close all;
clc;

v = 900:999;
M = v.'*v;
p = arrayfun(@(x) is_palindrome(x), M, 'un', 0);
p = cell2mat(p);
max(M(p))

function out = is_palindrome(x)
    x = num2str(x);
    l = length(x);
    out = strcmp(x(1:l/2), x(l:-1:1+l/2));
end