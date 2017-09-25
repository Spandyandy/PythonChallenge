inp = "fdasdfasd"
myList = [];
while len(inp) > 6 :  
	inp = input();
	myList.append(inp);

i = 0;
j = 0;
while i < len(myList) :
	while j < len(myList[i]) :
		if ord(myList[i][j]) > 96 and ord(myList[i][j]) <123 :
			print(myList[i][j], end='');
		j+=1;
	i+=1;
	j=0;
