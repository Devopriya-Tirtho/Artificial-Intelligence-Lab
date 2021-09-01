parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib'). grandparent(Z, X) :- parent(X, Y), parent(Y, Z).


findGp :- write(' Grandchild: '), read(X), write('Grandparent: '),
		grandparent(X, Gp), write(Gp), tab(5), fail.
findGp.

