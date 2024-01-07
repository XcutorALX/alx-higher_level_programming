#include "lists.h"
/**
 * reverse_list - reverses a linked list
 *
 * @head: the first node in the linked list
 *
 * Return: a pointer to the last node or NULL if list is empty
 */

listint_t *reverse_list(listint_t **head)
{
	struct listint_s *current, *tail;

	if (*head == NULL)
		return (NULL);

	tail = *head;
	current = *head;
	current->prev = NULL;

	while (current != NULL && current->next != NULL)
	{
		current->next->prev = current;
		current = current->next;
	}
	tail = current;

	return (tail);
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

	return (1);
}
