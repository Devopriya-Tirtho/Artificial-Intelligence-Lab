parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel'). parent('Rakib' , 'Rebeka'). parent('Rashid' , 'Hasib').
male('Hasib'). male('Rakib'). male('Sohel'). female('Rebeka'). brother(Y, Z) :- parent(X, Y), parent(X, Z),male(Z),not(Y=Z).


findBro :- write(' Name: '), read(Y), write('Brother: '),
brother(Y, Bro), write(Bro), tab(5), fail.
findBro.
