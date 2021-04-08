#include <stdio.h>
int main(){
    int a, b;
    printf("Enter first figure: " );
    scanf("%i", &a);
    printf("Enter second figure: " );
    scanf("%i", &b);
    while (a != b) {
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }
    printf("LCD: %i\n", a);
    getch();
}