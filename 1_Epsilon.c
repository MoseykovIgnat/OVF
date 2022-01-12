#include <math.h>
#include <stdio.h>
#include <typeinfo>
void espfinder(){
	double eps = 1;//Unit in the last place (Float - 4 Bite) (Double - 8 Bite)
	int rank = 0;
	int max_num = 0;
	double m=1;
	int i=0;
	while ((eps/2)+1 != 1){
		eps/=2;
		rank++;
	}
	while (isinf(m)==0){
		max_num=m;
		m*=2;
		i++;
		
	}

	printf("%d\n", i);
	printf("ULP is %.18f\n", eps);
	printf("Количество бит Мантиссы: %d\n", rank);


}

int main(){
espfinder();

}