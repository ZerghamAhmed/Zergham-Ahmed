//recovers images from jpeg files

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
        fprintf(stderr, "Usage: recover image\n");
        return 1;
    }

    // stores the infile, outfile, and names of recovered jpeg images
    char *infile = argv[1];
    FILE *outfile = NULL;
    char jpeg_filename[8];
    int jpeg_number = 0;

    // opens the memory card file
    FILE *inptr = fopen(argv[1], "r");

    // if it fails to open, then program terminates
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // create an array called buffer that stores the bytes for our memory card
    typedef uint8_t BYTE;
    BYTE buffer[512];

    // repeat reading the memory card until the end of the file
    while (fread(buffer, 512, 1, inptr) == 1)
    {
        // finds whether the current position is the start of a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if a jpeg file is already open, then closes it
            if (outfile != NULL)
            {
                fclose(outfile);
            }

            // will start recovering the jpeg and keeping track of them
            sprintf(jpeg_filename, "%03i.jpg", jpeg_number);
            outfile = fopen(jpeg_filename, "w");
            jpeg_number++;
        }
        // if a new jpeg is not found, then start back at the loop
        if (outfile != NULL)
        {
            fwrite(buffer, 512, 1, outfile);
        }
    }

    //end of mem card, exit loop close all files

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outfile);

    // success
    return 0;
}

