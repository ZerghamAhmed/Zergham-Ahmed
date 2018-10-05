# Questions

## What's `stdint.h`?

It is the header name that microsoft uses to store the code for all their primitive data types


## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

They are units of storage which can store more information since they are unsigned.


## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

A BYTE is 1 byte. A DWORD is 4 bytes, and LONG is also 4 bytes.


## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

The characters B and M in ASCII


## What's the difference between `bfSize` and `biSize`?

The bfSize is the size of the bitmap file in bytes. The biSize is the number of bytes the structure requires.

## What does it mean if `biHeight` is negative?

It means that top down DIBs (bitmaps with colors) cannot be compressed. Usually we take the absolute value of it to use it.


## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

It might not exist yet or might be corrupted.


## Why is the third argument to `fread` always `1` in our code? (For example, see lines 40, 44, and 75.)

Because we want to have one element/pixel.


## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

Changes the pointer’s location

## What is `SEEK_CUR`?

Is the beginning of the file
