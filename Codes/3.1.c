#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void r(char *str, int len)
{
int i;
double temp;
double value;
double ans;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = (double)rand()/RAND_MAX;
value=1-temp;
ans=-2*log(value);
fprintf(fp,"%lf\n",ans);
}
fclose(fp);

}

int  main(void) //main function begins
{
r("rand.dat",1000000);
return 0;
}
