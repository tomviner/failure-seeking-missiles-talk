#include <stdio.h>

int main()
{
    /* A nice long string */
    char string[2];

    printf( "Please enter a long string: " );

    /* notice stdin being passed in */
    fgets ( string, 2, stdin );

    printf( "You entered a very long string, %s", string );

    getchar();
}
