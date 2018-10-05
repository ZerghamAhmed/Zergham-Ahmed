// resizes a bmp file

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cs50.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    //accept a scale value given through the command line
    int scale_factor = atoi(argv[1]);

    // ensure proper usage
    if (argc != 4 || scale_factor < 0 || scale_factor > 100)
    {
        fprintf(stderr, "Usage: resize n infile outfile\n");
        return 1;
    }
    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");

    // if input file fails to open, end
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");

    // if output file fails to open, end program
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    // changes the bitmapfileheader by the scale factor and refers to the new one and its elements as nbf from here on out
    BITMAPFILEHEADER nbf = bf;

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    // changes the bitmapinfoheader by the scale factor and refers to the new one and its elements as nbi from here on out
    BITMAPINFOHEADER nbi = bi;

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // scales the height and width of the image by the scale factor
    nbi.biHeight = scale_factor * bi.biHeight;
    nbi.biWidth = scale_factor * bi.biWidth;

    // calculate old and new padding
    int old_padding = (4 - ((bi.biWidth) * sizeof(RGBTRIPLE)) % 4) % 4;
    int padding = (4 - ((nbi.biWidth) * sizeof(RGBTRIPLE)) % 4) % 4;

    nbi.biSizeImage = ((sizeof(RGBTRIPLE) * nbi.biWidth) + padding) * abs(nbi.biHeight);
    nbf.bfSize = nbi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&nbf, sizeof(BITMAPFILEHEADER), 1, outptr);
    // write outfile's BITMAPINFOHEADER
    fwrite(&nbi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterates over the scanline of the old image
    for (int i = 0; i < abs(bi.biHeight); i++)
    {
        // iterates over each pixel on a single row of the new image
        for (int j = 0; j < scale_factor; j++)
        {
            // iterates over each pixel on a single row of the old image
            for (int a = 0; a < bi.biWidth; a++)
            {
                // temporary storage for values
                RGBTRIPLE triple;
                // reads RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // horizontally copies each pixel over to the new image based on the above iterations
                for (int b = 0; b < scale_factor; b++)
                {
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
            }
            // adds the updated padding needed for the new image
            for (int k = 0; k < padding; k++)
            {
                fputc(0x00, outptr);
            }

            // vertically copies each pixel over to the new image
            if (j < scale_factor - 1)
            {
                fseek(inptr, -bi.biWidth * sizeof(RGBTRIPLE), SEEK_CUR);
            }

        }
        // skip over old padding
        fseek(inptr, old_padding, SEEK_CUR);
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;

}
