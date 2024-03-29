#include "lists.h"

/**
 * check_cycle - a function that checks if there is a cycle in a linked list
 *
 * @list: the linked list to check
 *
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	struct listint_s *fast, *slow;


	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
