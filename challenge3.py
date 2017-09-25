inp = "       "
myList = [];
while len(inp) > 6 :  
	inp = input();
	myList.append(inp);


print();
i = 0;
while i < len(myList)-1:
	j=3;
	while j < len(myList[i])-4:
		if myList[i][j].islower() and myList[i][j-3].isupper() and myList[i][j-2].isupper() and myList[i][j-1].isupper() and myList[i][j+1].isupper() and myList[i][j+2].isupper() and myList[i][j+3].isupper() and myList[i][j+4].islower() and myList[i][j-4].islower():
				count = 0;
				print(myList[i][j], end='');

		j+=1;
	i+=1;

print("\n");
