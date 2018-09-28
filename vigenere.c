#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
//make prototype for shift function which we will use in the program
//the shift function will be used to store each keyword's character as a integer value which will be used to shift each character
int shift(char c);
int main(int argc, string argv[])
{
//asks user for exactly one command line argument
    int key;
    if (argc == 2)
    {
//makes sure each character of the command line argument, which will be the key we will use to shift the message, is an alphabetical character
        for (int i = 0; i < strlen(argv[1]); i++)
        {
//if a character of the command line argument is not an alphabetical character, the program will terminate
            char check = argv[1][i];
            if (!isalpha(check))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
//if the command line argument is valid the program will continue and ask for a message
        string message = get_string("Plaintext: ");
        for (int i = 0, j = 0; i < strlen(message); i++)
        {
//each character of this message will be stored as an integer and have the shift function add each representative integer of the keyword
            key = shift(argv[1][j % strlen(argv[1])]);
            if (islower(message[i]))
            {
//if the character of the message is lowercase, the case will be preserved and the key will be added to it and wrapped around as needed
                message[i] = ((message[i] - 97 + key) % 26 + 97);
                j++;
            }
            else if (isupper(message[i]))
            {
//if the character of the message is uppercase, then the case will be preserved and the keys will be added to it and wrapped around as needed
                message[i] = ((message[i] - 65 + key) % 26 + 65);
                j++;
            }
        }
//the encrypted message which has been shifted according to the vigenere style of cipher encryption will be printed
        printf("Ciphertext: %s\n", message);
    }
//if user didn't provide exactly one command line argument, program will terminate
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
//here we make a function that will be used in our program to shift each character of our message
//it will do this by representing each letter in the alphabet with numbers 0 to 25, 0 being A and a, and 25 being Z and z
int shift(char c)
{
    int num;
    if (islower(c))
    {
        num = c - 97;
        return num;
    }
    else
    {
        num = c - 65;
        return num;
    }
}







