inputs = input();
i = 0;
while i < len(inputs):
	if ord(inputs[i])>96 and ord(inputs[i])<123:
		print(chr((ord(inputs[i])-95)%26+97), end='');
	else:
		print(inputs[i], end='');
	i += 1;
