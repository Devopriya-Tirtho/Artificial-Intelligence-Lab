parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Hasib' , 'Sakib'). male('Hasib'). male('Rakib'). male('Sohel'). male('Sakib'). female('Rebeka'). grandparent(M, Z) :-
	parent(X, M), parent(Y, X), parent(Y, Z), male(Z), not(X=Z).

findUn :- write(' Name: '), read(M), write('Uncle: '),
grandparent(M, Un), write(Un), tab(5), fail.
findUn.
