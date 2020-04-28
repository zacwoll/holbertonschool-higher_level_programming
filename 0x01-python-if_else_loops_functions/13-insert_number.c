#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert a node in a sorted linked list
 * @head: linked list
 * @number: new node->n
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current = *head;

    if (!head)
        return NULL;

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else if (number < current->n)
    {
        new->next = current;
        *head = new;
    }
    else
    {
        while (current->next && number > current->next->n)
            current = current->next;
        new->next = current->next;
        current->next = new;
    }

    return (new);
}
