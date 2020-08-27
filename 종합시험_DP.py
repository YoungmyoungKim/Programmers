def solution():




"""
# coins: array of coins
# N : number of coins

for(int i=0;i<=N;i++) {
	for(int j=0;j<=X;j++) {
		table[i][j] = 0x0ffffff;
	}
}

table[0][0] = 0
for(int i=1;i<=N;i++) {

	for(int j=coins[i];j<=X;j++) {
		if( table[i-1][j] > table[i][j-coin[i]] + 1 )
			table[i][j] = table[i][j-coin[i]] + 1
		else
			table[i][j] = table[i-1][j]
	}
}"""
