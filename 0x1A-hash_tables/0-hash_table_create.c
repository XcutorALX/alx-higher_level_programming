#include "hash_tables.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * hash_table_create - creates an empty hash table
 *
 * @size: the size of the table to create
 *
 * Return: returns a pointer to the hash table
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *newTable;

	if (size == 0)
		return (NULL);

	newTable = malloc(sizeof(hash_table_t));

	if (!newTable)
		return (NULL);

	newTable->size = size;
	newTable->array = calloc(size, sizeof(hash_node_t *));

	if (!(newTable->array))
	{
		free(newTable);
		return (NULL);
	}

	return (newTable);
}
