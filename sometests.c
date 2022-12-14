#include <stdio.h>
#include <stdlib.h>
#include <string.h>
enum { SIZE = 8 };
int main(void)
{
    // trivial example
    int array[SIZE], n = 0;
    while(n < SIZE) array[n++] = rand() % 2;
    
    puts("Array filled!");
    n = 0;
    while(n < SIZE) printf("%d ", array[n++]);
    printf("\n");
 
    // classic strcpy() implementation
    // (copies a null-terminated string from src to dst)
    char src[]="Hello, world", dst[sizeof src], *p=dst, *q=src;
    while(*p++ = *q++)
        ; // null statement
    puts(dst);
}



