#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted linked list
 *
 *@head: the head of the linked list
 *@number: the number to be inserted
 *
 * Return: returns a pointer to the new node created
 */

listint_t *insert_node(listint_t **head, int number)
{
	struct listint_s *ptr, *newNode;


	ptr = *head;
	while (ptr != NULL)
	{
		if (ptr->next == NULL)
		{
			newNode = add_nodeint_end(head, number);
			return (newNode);
		}

		if (ptr->n <= number && ptr->next->n > number)
		{
			newNode = malloc(sizeof(struct listint_s));
			if (!newNode)
				return (NULL);
			newNode->n = number;
			newNode->next = ptr->next;
			ptr->next = newNode;
			return (newNode);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
