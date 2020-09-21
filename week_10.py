import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def __str__(self):
        return f'{self.vertices}'

    def shortest_path(self, start, finish):
        print("Finding shortest path")
        pq = []
        distance = {}
        previous = {}
        # set up
        for vertex in self.vertices:
            print(f'adding {vertex} to pq')
            if vertex == start:
                distance[vertex] = 0    # set the start distance to 0
                heapq.heappush(pq, [0, vertex])
            else:
                distance[vertex] = float("inf")
                heapq.heappush(pq, [float("inf"), vertex])
            previous[vertex] = None

        while len(pq) != 0:
            # get the vertex with the smallest distance
            smallest = heapq.heappop(pq)
            smallest_vertex = smallest[1]
            if smallest_vertex == finish:

                path = []
                while previous[smallest_vertex]:
                    print(f'adding {smallest_vertex}')
                    path.append(smallest_vertex)
                    smallest_vertex = previous[smallest_vertex]
                print(f"Finished: {path}")
                return path

            if distance[smallest_vertex] == float("inf"):
                print("No path to destination")
                break

            for neighbour in self.vertices[smallest_vertex]:
                # alternate path
                alt = distance[smallest_vertex] + self.vertices[smallest_vertex][neighbour]

                if alt < distance[neighbour]:
                    distance[neighbour] = alt
                    previous[neighbour] = smallest_vertex
                    for n in pq:
                        if n[1] == neighbour:
                            # update the priority queue with the new shortest distance
                            n[0] = alt
                            break
                    heapq.heapify(pq)
        return distance


if __name__ == "__main__":
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