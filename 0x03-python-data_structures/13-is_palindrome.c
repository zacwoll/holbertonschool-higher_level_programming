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
	listint_t *slow = *head, *fast = *head;
	
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	slow = reverse_list(&slow);
	fast = *head;
	while (fast && slow)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}
