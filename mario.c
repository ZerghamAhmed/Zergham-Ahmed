#include <cs50.h>
#include <stdio.h>

int height(string prompt);
int main(void)
{
    int h = height("How tall should the pyramid be? (pick a number between 1 and 8)\n");
 // Print number of hashes based on input
    for(int i = 0; i < h; i++)
    {
        for(int a = 0; a < h-i; a++)
        {
            printf(" ");
        }    
        for(int j = 0; j < i + 1; j++)
        { 
            printf("#");
        }   
        printf("\n");
    }
}

// Prompt user for height falling between 1 and 8
int height(string prompt)
{
    int h;
    do
    {
        h = get_int("%s", prompt);
    }
    while (h < 1 || h > 8);
    
    return h;
}
    

        



 

