#include <stdio.h>

int main()
{
    int i, n;
    n = 256;
    char input[n];
    fgets( input, n, stdin );
    // printf( "You entered a very long string, '%s'\n", input );

    for ( i = 0; i < n-1; i++ )
    {
        if ( input[i] != 'w' )
        {
            // printf( "you '%c'\n", input[i]);
            return 0;
            // input[i+200] = 'z';
        }
    }
    return 1/0;

    // printf( "You entered a very long string, %s", input  );

    // getchar();
}


