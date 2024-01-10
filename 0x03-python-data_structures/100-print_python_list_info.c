#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints a python list object and it's info
 *
 * @p: a pointer to a python object
 *
 * Return: none
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *item;
	long int size, index;

	if (p == NULL)
		return;
	if (PyList_Check(p) == 1)
	{
		size = PyList_Size(p);
		list = (PyListObject *)p;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);

		for (index = 0; index < size; index++)
		{
			item = PyList_GET_ITEM(p, index);
			printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
		}
	}
}
