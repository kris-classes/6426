"""
ISCG6426 - Dijkstra's algorithm - Single-source shortest path
"""
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def __str__(self):
        return f'{self.vertices}'

    def shortest_path(self, start, finish):
        print(f'Finding shortest path between {start} and {finish}')
        pq = []
        distance = {}
        previous = {}
        # set up
        for vertex in self.vertices:
            if vertex == start:
                distance[vertex] = 0    # set the start distance to 0
                heapq.heappush(pq, [0, vertex])
                print(f'Distance from {vertex} to {vertex} set to 0')
            else:
                distance[vertex] = float('inf')
                heapq.heappush(pq, [float('inf'), vertex])
                print(f'Distance from {start} to {vertex} set to infinity')
            previous[vertex] = None

        while len(pq) != 0:  # Can also do 'while pq'
            # Get the vertex with the smallest distance
            smallest = heapq.heappop(pq)
            # Get the vertex name from [distance, vertex_name] in queue.
            smallest_vertex = smallest[1]
            # Found the shortest distance to the finish.
            if smallest_vertex == finish:
                # Create an empty path.
                path = []
                while previous[smallest_vertex]:
                    path.insert(0, smallest_vertex)
                    smallest_vertex = previous[smallest_vertex]
                # Add the start and finish vertices.
                path.insert(0, start)
                path.append(finish)
                print(f'Finished: {" -> ".join(path)}. Total distance: {smallest[0]}')
                return path

            if distance[smallest_vertex] == float('inf'):
                print("No path from {stat} to {finish} vertex")
                break

            for neighbour in self.vertices[smallest_vertex]:
                # Calculate the new alternate distance
                # Using the old distance + the new one
                alt = distance[smallest_vertex] + self.vertices[smallest_vertex][neighbour]

                # Compare if the new distance is shorter.
                if alt < distance[neighbour]:
                    print(f'{smallest_vertex} -> {neighbour} changed from {distance[neighbour]} to {alt}')
                    # If it is, update the distance.
                    distance[neighbour] = alt
                    previous[neighbour] = smallest_vertex
                    for n in pq:
                        if n[1] == neighbour:
                            # Update the priority queue with the new shortest distance
                            n[0] = alt
                            break
                    heapq.heapify(pq)
        # Return all the distances.
        print(f'Final Distances: {distance}')
        return distance


if __name__ == "__main__":
    # Simple graph from Lecture 10
    g = Graph()
    g.add_vertex("A",{'B': 1, 'C': 3, 'E': 3})
    g.add_vertex("B", {'A': 1, 'D': 4})
    g.add_vertex("C", {'A': 3, 'E': 9, 'F': 1})
    g.add_vertex("D", {'B': 4, 'E': 7})
    g.add_vertex("E", {'D': 4, 'C': 9, 'A': 3})
    g.add_vertex("F", {'C': 1})
    g.add_vertex("X", {'Y': 15})
    g.add_vertex("Y", {'X': 15})
    # print(g)
    g.shortest_path("D", "F")


    # Data from Google Maps
    north_island = Graph()
    north_island.add_vertex('Cape Reinga', {
        'Whangarei': 276,
    })
    north_island.add_vertex('Whangarei', {
        'Cape Reinga': 276,
        'Auckland': 158,
    })
    north_island.add_vertex('Auckland', {
        'Whangarei': 158,
        'Hamilton': 122,
        'Tauranga': 218,
    })
    north_island.add_vertex('Tauranga', {
        'Auckland': 218,
        'Gisborne': 262,
        'Hamilton': 114,
        'Rotorua': 67,
    })
    north_island.add_vertex('Hamilton', {
        'Auckland': 122,
        'New Plymouth': 237,
        'Rotorua': 134,
        'Taupo': 155,
        'Tauranga': 114,
        'Palmerston North': 394,
        'Wellington': 520,
    })
    north_island.add_vertex('Rotorua', {
        'Tauranga': 67,
        'Hamilton': 134,
        'Gisborne': 271,
        'Taupo': 80,
    })
    north_island.add_vertex('Gisborne', {
        'Tauranga': 262,
        'Rotorua': 271,
        'Napier': 212,
    })
    north_island.add_vertex('Taupo', {
        'Hamilton': 155,
        'Rotorua': 80,
        'Palmerston North': 243,
        'New Plymouth': 278,
        'Napier': 141,
    })
    north_island.add_vertex('New Plymouth', {
        'Hamilton': 237,
        'Taupo': 278,
        'Palmerston North': 234,
    })
    north_island.add_vertex('Napier', {
        'Taupo': 141,
        'Gisborne': 212,
        'Palmerston North': 183,
    })
    north_island.add_vertex('Palmerston North', {
        'New Plymouth': 234,
        'Napier': 183,
        'Hamilton': 394,
        'Taupo': 243,
        'Wellington': 139,
    })
    north_island.add_vertex('Wellington', {
        'Palmerston North': 139,
    })
    
    # Was going to add the South Island but I think this is enough for helping to understand it.

    print('===\n')
    north_island.shortest_path('Cape Reinga', 'Wellington')
    print('===\n')
    north_island.shortest_path('New Plymouth', 'Gisborne')
