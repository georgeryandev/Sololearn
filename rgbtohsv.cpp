// Another attempt at creating a function that converts RGB into HSV.


#include <iostream>

using namespace std;

int getMax(int a, int b, int c) {
    if (a > b && a > c)
        return a;
    if (b > a && b > c)
        return b;
    if (c > a && c > a)
        return c;
    return 0;
}

int getMin(int a, int b, int c) {
    if (a < b && a < c)
        return a;
    if (b < a && b < c)
        return b;
    if (c < a && c < a)
        return c;
    return 0;
}
int * rgb2hsv(int r, int g, int b) {
    int rValue=r/255;
    int gValue=g/255;
    int bValue=b/255;
    
    int h=0;
    int s;
    int v;
    
  
    
    int Cmax=getMax(rValue, gValue, bValue);
    int Cmin=getMin(rValue, gValue, bValue);
    
    int delta=Cmax-Cmin;
    
    if(delta > 0){
       if(Cmax==rValue)
            h=60*((gValue-bValue)/delta)%6;
       if (Cmax == gValue)
            h=60*(((bValue*delta)-rValue)/delta)+2;
       if (Cmax== bValue) 
            h=60*(((rValue*delta)-gValue)/delta)+4;
    }
    if(Cmax > 0) {
        s=delta/Cmax;
    }
    else {
        s=0;
    }
    
    v=Cmax;
    
   int hsv[] = {h, s, v};
    
    return hsv;
}


int main()
{
   int * x = rgb2hsv(255, 242, 243);
   cout << x[0];
}
