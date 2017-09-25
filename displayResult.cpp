#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	FILE* fpr = fopen("pridict_text_data.txt", "r");
	FILE* fpw = fopen("sample_submission.txt", "w");
	fprintf(fpw, "id,label\n");
	
	for (int i = 0; i < 282796; i++) {
		fprintf(fpw, "%d,", i);
		
		double t;
		fscanf(fpr, "%lf", &t);
		fprintf(fpw, "%.6lf\n", t);
	}
	fclose(fpr);
	fclose(fpw);
	return 0;
} 
