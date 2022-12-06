#include <stdio.h>
#include "lists.h"

/**
 * reverse_t - This function reverse a linked list.
 * @head: The pointer to the head of the linked list
 * Return: The pointer to the reversed linked list
 */
listint_t *reverse_t(listint_t **head)
{
	listint_t *current, *prev, *next;

	current = *head;
	prev = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - This function checks if a linked list is palidrome
 * @head: This is the pointer the head of the linked list.
 * Return: 1 if is a palindrome or 0 if it not
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev, *current;

	rev = reverse_t(head);
	current = *head;
	while (current != NULL)
	{
		if (current->n == rev->n)
		{
			rev = rev->next;
			current = current->next;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
