parent('Hasib','Rakib').parent('Rakib','Sohel').parent('Rakib','Sohel').Parent('Rashid','Hasib').brother(Y,Z):-parent(X,Y)
,parent(X,Z).
findbr:-write('Name:'),read(Y),write('Brother/Sister:'),brother(Y,br),write(br),tab(5),
	fail.
findbr.
