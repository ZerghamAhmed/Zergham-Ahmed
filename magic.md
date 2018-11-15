# Like Magic

## Questions

4.1. BM

4.2. %PDF

4.3. Your program will read the first few magic numbers which indicate
a particular file type, but the file could also have random binary data,
although this is not common.

4.4. When you use bitwise operators you do work on the bits of the operands by
multipling the binary of representation of one operand by the binary of the other.
So in this case, 0xf0 can be represented by 11110000 and exe0 is represented by
11100000. We know we want the buffer to be equal to either 0xe0, 0xe1, etc. With the bitwise operator,we take the binary of, for example, 0xe6, which is 11100110 and multiply it by the binary for 0xf0
which results in 11100000. All of the possible combinations of the fourth byte result in this same binary number when you use the bitwise operator on it and 0xf0, because of the nature of all of the fourth
bytes having a 0 for the 4th column to the right, so each of the fourth bytes result in the same bitwise operation and so you can use that operation's result and compare 0xf0 to exe0 (which represents all other
fourth bytes) to determine whether the image is a JPEG

4.5. It is more efficient because the bitwise OR will change the bit to 1 if either bits is 1 and zero only when both bits are 0.
Therefore, you will need more == comparisons than if you just used the bitwise AND since it will change the 0s at the beginning of the 0xf0, making the comparison in a manner similar to the one described in the
previous quesiton, but with more comparisons.

4.6. See `magic.c`.

## Debrief

a.
4.3
https://stackoverflow.com/questions/47882/what-is-a-magic-number-and-why-is-it-bad

4.4
https://www.youtube.com/watch?v=XLkVD2yQAEM


b. 80 minutes
