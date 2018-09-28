#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
//makes the user enter exactly one command line argument
    int key;
    if (argc == 2)
    {
//check that every character of the string is a digit or else terminate
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            char check = argv[1][i];    
            if (!isdigit(check))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        } 
        key = atoi(argv[1]);
    }
//if the user didn't enter in one command line argument, then terminates
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
//if the user entered a number as the command line argument continues...
//asks for a plaintext message, after encrypting the message - it will show ciphertext at end
    string message = get_string("Plaintext: ");
    printf("Ciphertext: ");
//stores each character of the message into a digit which will then have the key added to it, separate clauses for lowercase and uppercase
    for (int i = 0; i < strlen(message); i++)
    {
//if the message has a lowercase letter, it wraps around its ascii value in the lowercase ascii range and shifts the character by the value of the key
        if (islower(message[i]))
        {
            char c = message[i];
            printf("%c", ((c - 97 + key) % 26 + 97));
        }
//if it is uppercase, it wraps around its ascii value in the uppercase ascii range and shifts the character by the value of the key
        else if (isupper(message[i]))
        {
            char c = message[i];
            printf("%c", ((c - 65 + key) % 26 + 65));
        }
//if anything other than alphabetic characters are used, like symbols, it will preserve it
        else
        {
            printf("%c", message[i]);
        }    
    }
    printf("\n");
}
//shows converted ciphertext aka the encrypted message - the code is written above by plaintexts' -
