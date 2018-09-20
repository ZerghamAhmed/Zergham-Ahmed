#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
 //collect correct input
    float f;
    {
    do
    {
        f = get_float("Change owed: ");
        
    }
    while (f <= 0);
    }
//convert to cents as needed
    int cents = round(f*100);
      int q;
      int d;
      int n;
      int p;
      
//do math for quarters, x is left over coins
    q = cents/25;
    cents = cents%25;
        
//do math for dimes
    d = cents/10;
    cents = cents%10;
        
//do math for nickels
    n = cents/5;
    cents = cents%5;
        
//do math for pennies
    p = cents/1;
    
printf("%i\n", q+d+n+p);
    
} 
   
    

    
        
    
