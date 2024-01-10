#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - prints details about a python byte object
 *
 * @p: a pointer to the byte object
 */

void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) != 1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str, &size);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size < 10)
		printf("  first %ld bytes:", size);
	else
		printf("  first 10 bytes:");

	for (i = 0; i <= size && i < 10; i++)
		printf("  %02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - prints info about a python list object
 *
 * @p: a pointer to the python list object
 */

void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int index;
	PyListObject *list = (PyListObject *)p;

	if (PyList_Check(p) != 1)
		return;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List  = %ld\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	for (index = 0; index < size; index++)
	{
		printf("Element %d: %s\n", index, list->ob_item[index]->ob_type->tp_name);
		if (!strcmp(list->ob_item[index]->ob_type->tp_name, "bytes"))
                        print_python_bytes(list->ob_item[index]);
	}

}
