#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main() {
	FILE* fpr1 = fopen("pridict_text_data.txt", "r");
	FILE* fpr2 = fopen("data/pridict_text_data2.txt", "r");
	FILE* fpr3 = fopen("data/pridict_text_data.txt", "r");
	
	FILE* fpw = fopen("sample_submission.txt", "w");
	fprintf(fpw, "id,label\n");
	
	for (int i = 0; i < 282796; i++) {
		fprintf(fpw, "%d,", i);
		
		double t1, t2, t3, t4;
		fscanf(fpr1, "%lf", &t1);
		fscanf(fpr2, "%lf", &t2);
		fscanf(fpr3, "%lf", &t3);
		
		if (i == 2) {
			printf("%lf, %lf, %lf\n", t1, t2, t3);
		}
		double t = exp(0.3 * log(t1) + 0.4 * log(t2) + 0.3 * log(t3));
		
		fprintf(fpw, "%.7lf\n", t);
	}
	fclose(fpr1);
	fclose(fpr2);
	
	fclose(fpr3);
//	fclose(fpr4);
	fclose(fpw);
	return 0;
} 
