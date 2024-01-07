#include "lists.h"
#include <stdlib.h>
/**
 * reverse_list - reverses a linked list
 *
 * @head: the first node in the linked list
 *
 * Return: a pointer to the last node or NULL if list is empty
 */

listint_t *reverse_list(listint_t **head)
{
	struct listint_s *current, *temp, *rev;

	if (*head == NULL)
		return (NULL);

	rev = malloc(sizeof(listint_t));
	rev->n = (*head)->n;
	rev->next = NULL;
	current = *head;

	while (current != NULL && current->next != NULL)
	{
		current = current->next;
		temp = rev;
		rev = malloc(sizeof(listint_t));
		rev->n = current->n;
		rev->next = temp;
	}

	return (rev);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: the first node in the linked list
 *
 * Return: 1 if it is a palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	struct listint_s *tail, *forward, *backward;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	
	tail = reverse_list(head);
	forward = *head;
	backward = tail;

	while (forward != NULL && backward != NULL && forward != backward)
	{
		if (forward->n != backward->n)
			return (0);

		forward = forward->next;
		backward = backward->next;
	}
	free_listint(tail);
	return (1);
}
