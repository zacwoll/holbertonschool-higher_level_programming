#include "lists.h"

/**
 * check_cycle - Check if a linked list has a cycle in it
 * @list: The list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *hare = list;

	while (tort && hare && hare->next)
	{
		tort = tort->next;
		hare = hare->next->next;

		if (tort == hare)
			return (1);
	}

	return (0);
}
