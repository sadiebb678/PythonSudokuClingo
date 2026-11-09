% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

#const s = 3. %constant nxn base subgrid to which expansion is done
#const ss = 9.
x(1..ss). %col val from 1 -> n (curr a 4x4 grid)
y(1..ss). %row val from 1 -> n (curr a 4x4 grid)
n(1..ss). %value from digits 1->9

%Initialize sudoku grid to have initial values
sudoku(X,Y,N) :- initial(X,Y,N).

% Make a set of all possible digits N for each cell X,Y pair
1{sudoku(X,Y,N) : n(N)}1 :- x(X), y(Y), not initial(X,Y,_).

subgrid(X,Y,A,B) :- x(X), x(A), y(Y), y(B), (X-1)/s == (A-1)/s, (Y-1)/s == (B-1)/s.

:- sudoku(X,Y,N), sudoku(A,Y,N), X!=A. %Remove repeats in same row
:- sudoku(X,Y,N), sudoku(X,B,N), Y!=B. %Remove repeats in same collum.
:- sudoku(X,Y,N), sudoku(A,B,N), subgrid(X,Y,A,B), X != A. %Remove repeats in same subgrid
:- sudoku(X,Y,N), sudoku(A,B,N), subgrid(X,Y,A,B), Y != B. %Remove repeats in same subgrid
:- sudoku(X,Y,N), sudoku(A,B,N), subgrid(X,Y,A,B), (X,Y) != (A,B). %Remove repeats in same subgrid

#show sudoku/3.
