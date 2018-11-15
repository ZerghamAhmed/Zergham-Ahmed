// checks file type

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    // make sure that program is properly used
    if (argc != 2)
    {
        fprintf(stderr, "Usage: determine file type\n");
        return 1;
    }

    // stores the infile
    char *infile = argv[1];

    // opens the file
    FILE *inptr = fopen(argv[1], "r");

    // if file cannot be opened or read
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // create an array called buffer that stores the bytes for our file
    typedef uint8_t BYTE;
    BYTE buffer[512];

    // repeat reading the memory card until the end of the file
    while (fread(buffer, 4, 1, inptr) == 1)
    {

        // finds whether the file is a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // label as JPEG
            printf("JPEG\n");
        }


        // finds whether the file is a BMP
        if (buffer[0] == 0x42 && buffer[1] == 0x4d)
        {
            // label as BMP
            printf("BMP\n");
        }


        // finds whether the file is a pdf
        if (buffer[0] == 0x25 && buffer[1] == 0x50 && buffer[2] == 0x44 && buffer[3] == 0x46)
        {
            // label as PDF
            printf("PDF\n");
        }

    }

    //end of file, exit loop close all files

    // close infile
    fclose(inptr);

    // success
    return 0;
}


