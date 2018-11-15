// C program to print a song using recursion
# include <stdio.h>



void sing(void)
{
        printf("This is the song that doesn't end.");
        printf("Yes, it goes on and on my friend.");
        printf("Some people started singing it not knowing what it was,");
        printf("And they'll continue singing it forever just because...");
        sing();
}

int main(void)
{
    sing();



}

// def main():
//     sing()


// def sing():
//     print("This is the song that doesn't end.")
//     print("Yes, it goes on and on my friend.")
//     print("Some people started singing it not knowing what it was,")
//     print("And they'll continue singing it forever just because...")
//     sing()


// if __name__ == "__main__":
//     main()