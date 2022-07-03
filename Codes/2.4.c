#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;
}

double variance(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;
double m=mean(str);
fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+pow(x-m,2);
}
fclose(fp);
temp = temp/(i-1);
return temp;
}
int main()
{
printf("%lf\n",mean("gau.dat"));
printf("%lf\n",variance("gau.dat"));
return 0;
}
