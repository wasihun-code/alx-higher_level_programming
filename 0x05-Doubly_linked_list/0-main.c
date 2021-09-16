#include "lists.h"

int main()
{
    struct node *root = NULL;
    struct node *first = (struct node*)malloc(sizeof(struct node));
    struct node *second= (struct node*)malloc(sizeof(struct node));
    struct node *third = (struct node*)malloc(sizeof(struct node));

    first->left = NULL;
    first->data = 10;
    first->right = second->left;
    root = first->left;

    second->left = first->right;
    second->data = 20;
    second->right = third->left;

    third->left = second->right;
    third->data = 30;
    third->right = NULL;

    display(root);
    return (0);
}
