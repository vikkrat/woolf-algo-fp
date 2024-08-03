import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, node, weight):
        heapq.heappush(self.heap, (weight, node))

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

def dijkstra(graph, start):
    # Ініціалізація
    min_heap = MinHeap()
    min_heap.push(start, 0)

    # Відстані від стартової вершини до всіх інших
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Відвідані вершини
    visited = set()

    while not min_heap.is_empty():
        current_weight, current_vertex = min_heap.pop()

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_weight + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                min_heap.push(neighbor, distance)

    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)

    print(f"Відстані від вершини {start_vertex} до всіх інших:")
    for vertex, distance in distances.items():
        print(f"Відстань до {vertex}: {distance}")
