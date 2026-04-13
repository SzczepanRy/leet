#mini

def parent(i): return (i - 1) // 2
def left_child(i): return 2 * i + 1
def right_child(i): return 2 * i + 2

def sift_up(heap, i):
    """Naprawa kopca w górę."""
    p = parent(i)
    if i > 0 and heap[i] < heap[p]:
        heap[i], heap[p] = heap[p], heap[i]
        sift_up(heap, p)

def sift_down(heap, i, length=None):
    """Naprawa kopca w dół."""
    if length is None:
        length = len(heap)

    smallest = i
    l = left_child(i)
    r = right_child(i)

    if l < length and heap[l] < heap[smallest]:
        smallest = l
    if r < length and heap[r] < heap[smallest]:
        smallest = r

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        sift_down(heap, smallest, length)

def heap_insert(heap, value):
    """Dodawanie elementu."""
    heap.append(value)
    sift_up(heap, len(heap) - 1)

def heap_extract_min(heap):
    """Usuwanie i zwracanie najmniejszego elementu."""
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()

    min_val = heap[0]
    heap[0] = heap.pop()
    sift_down(heap, 0)
    return min_val

def build_heap(data):
    """Budowanie kopca z listy (w miejscu)."""
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(data, i)
    return data

def heap_sort(data):
    """Sortowanie przez kopcowanie."""
    # 1. Budujemy kopiec
    build_heap(data)
    sorted_list = []
    # 2. Wyciągamy elementy
    # Uwaga: aby nie niszczyć oryginału, pracujemy na kopii
    temp_heap = data.copy()
    while temp_heap:
        sorted_list.append(heap_extract_min(temp_heap))
    return sorted_list

# --- PRZYKŁAD UŻYCIA ---
numbers = [10, 4, 8, 2, 1]

# Budowanie
build_heap(numbers)
print(f"Zbudowany kopiec: {numbers}")

# Wstawianie
heap_insert(numbers, 0)
print(f"Po wstawieniu 0:  {numbers}")

# Usuwanie
m = heap_extract_min(numbers)
print(f"Wyjęte min ({m}):  {numbers}")

# Sortowanie
raw = [15, 3, 7, 1, 9]
print(f"Posortowane:      {heap_sort(raw)}")
