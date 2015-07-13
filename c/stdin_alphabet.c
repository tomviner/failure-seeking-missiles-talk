#include <stdio.h>

int main()
{
    int i, n;
    n = 10;
    char input[n];
    fgets( input, n, stdin );
    printf( "You entered a very long string, '%s'\n", input );
    printf( "atoi: '%i'\n", 1);
    printf( "atoi: '%c'\n", input[2]);
    printf( "'a' - '0': '%i'\n", 'a' - '0');

    for ( i = 0; i < n-1; i++ )
    {
        printf( "(%c) input[i] - '0': '%i'\n", input[i], input[i] - '0');
        printf( "'a' - '0' + %i: '%i'\n", i, 'a' - '0' + i);
        if ( (input[i] - '0') != ('a' - '0' + i) )
        {
            printf( "you '%c'\n", input[i]);
            return 0;
            // input[i+200] = 'z';
        }
        printf( "\n");
    }
    return 1/0;

    printf( "You entered a very long string, %s", input  );

    // getchar();
}


