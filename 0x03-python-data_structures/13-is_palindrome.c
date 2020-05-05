#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - determines if singly linked list is palindrome
 * @head: head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	unsigned int n = 0, i, j;
	int *arr;

	current = *head;
	if (!current)
		return (1);
	while (current)
	{
		n++;
		current = current->next;
	}
	arr = malloc(sizeof(int) * n);
	n = 0;
	current = *head;
	while (current)
	{
		arr[n] = current->n;
		current = current->next;
		n++;
	}
	for (i = 0, j = n - 1; i < j; i++, j--)
	{
		printf("%d : %d\n", arr[i], arr[j]);
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
