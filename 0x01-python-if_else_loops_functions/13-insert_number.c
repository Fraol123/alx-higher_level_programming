#include "lists.h"

/**
 * insert_node - Entry Point
 *
 * @head: the list passed in
 * @number: value of the new node
 *
 * Description: Inserts a node in an ordered linked list
 *
 * Return:  The address of the new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *newNode, *firstNode;

firstNode = *head;

newNode = malloc(sizeof(listint_t));
if (newNode == NULL)
return (NULL);
newNode->n = number;

if (*head == NULL || (*head)->n > number)
{
newNode->next = *head;
*head = newNode;
return (newNode);
}

while (firstNode->next != NULL)
{
if ((firstNode->next)->n >= number)
{
newNode->next = firstNode->next;
firstNode->next = newNode;
return (newNode);
}
firstNode = firstNode->next;
}
firstNode->next = newNode;
newNode->next = NULL;
return (newNode);
}
