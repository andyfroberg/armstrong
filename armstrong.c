#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "armstrong.h"

int main()
{
    int userNumber = 0;
    printf("Enter a number to verify if it is an Armstrong number: ");
    scanf("%d", &userNumber);
    printf("Is %d an Armstrong number?: %s\n", userNumber,  isArmstrongNumber(userNumber) ? "true" : "false");
    return 0;
}

bool isArmstrong(int candidate)
{
    int numberOfDigits = getNumberOfDigits(candidate);
    int sum = 0;
    for (int i = candidate; i != 0; i /= 10)
    {
	    int num = i % 10;
	    int n = 1;
	    for (int j = 0; j < numberOfDigits; j++)
		{
			n *= num;
		}
	    sum += n;
    }
    return sum == candidate;
}

int numDigits(int num)
{
    int len = 0;
    while (num != 0)
    {
        num /= 10;
        len++;
    }
    return sum;
}
