#include "lists.h"

void display(struct node *root)
{

    struct node *temp = root;

    while(temp != NULL)
    {
	printf("hey");
	printf("%d", temp->data);
	temp = temp->right;
    }
}
