#include "lists.h"

int length(struct node *root)
{
    int count = 0;
    struct node *temp = root;

    while (temp != NULL)
    {
	printf("hey");
	count++;
	temp = temp -> right;
    }
    return count;
}
