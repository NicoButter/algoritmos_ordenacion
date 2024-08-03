def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # La última i posiciones están ordenadas
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia si el elemento encontrado es mayor
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort:", bubble_sort(arr))