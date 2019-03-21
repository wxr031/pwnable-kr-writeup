#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	srand(time(NULL));
	int random[8];
	for (int i = 0; i <= 7; i++) {
		random[i] = rand();
	}
	int hash;
	scanf("%d", &hash);
	int canary = hash - (random[4] - random[6] + random[7] + random[2] - random[3] + random[1] + random[5]);
	printf("%d\n", canary);
}

