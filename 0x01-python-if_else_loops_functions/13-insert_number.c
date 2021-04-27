#include "lists.h"
#include <stdlib.h>
/**
 *insert_node- inserts into a sorted singly linked list
 *@head:pointer to pointer of first node of listint_t list
 *@number: the number to be inserted
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = *head;
listint_t *newp = malloc(sizeof(listint_t));
newp->number = number;
newp->next = NULL;

int key = number;
if (*head == NULL || key < *head->number)
{
newp->next = *head;
*head = newp;
}
else
{
temp = *head;
while (temp->next != NULL && temp->next->number < key)
temp = temp->next;
newp->next = temp->next;
temp->next = newp;
}
return (*head);
}
