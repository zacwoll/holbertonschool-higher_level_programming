#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * reverse_list - Reverse a linked list
 * @head: The list
 * Return: ptr to new head
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - determines if singly linked list is palindrome
 * @head: head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head, *one, *two;
	
	while (hare && hare->next)
	{
		hare = hare->next->next;
		one = tortoise;
		tortoise = tortoise->next;
	}

	tortoise = reverse_list(&tortoise);
	two = tortoise;
	hare = *head;
	while (hare && tortoise)
	{
		if (hare->n != tortoise->n)
			return (0);
		hare = hare->next;
		tortoise = tortoise->next;
	}
	tortoise = reverse_list(&two);
	one->next = tortoise;
	return (1);
}
