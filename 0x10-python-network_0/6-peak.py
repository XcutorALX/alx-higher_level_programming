def find_peak(listint):
    """
    Finds a peak in a list of unsorted integers using recursive binary search.

    Args:
        listint (list): List of unsorted integers.

    Returns:
        int: The peak element.
    """
    # Base case: if the list is empty, return None
    if not listint:
        return None

    # Find the middle index
    mid = len(listint) // 2

    # Compare the middle element with its neighbors (if they exist)
    if (mid == 0 or listint[mid - 1] <= listint[mid]) and \
       (mid == len(listint) - 1 or listint[mid + 1] < listint[mid]):
        return listint[mid]
    elif mid > 0 and listint[mid - 1] > listint[mid]:
        # If the left neighbor is greater, recursively search the left half
        return find_peak(listint[:mid])
    else:
        # Otherwise, recursively search the right half
        return find_peak(listint[mid:])
