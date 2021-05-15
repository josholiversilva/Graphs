INF = 99999

# Dijkstra
def dijkstra(graph):
    pass


# Floyd-Warshall Cycle Detection
def floyd(graph):
    pass
# Bellman Ford

# Weighted
#        8>
#    (1) -- (3)
#  4>/    2>|  \3>
#   /       |   \
# (0)      (4)   (6)
#   \  9>/  |   /
#  8>\ /    | / 2>
#    (2) -- (5)
#         1>

graph = [
    [ 0 , 4 , 8 ,INF,INF,INF,INF],
    [INF, 0 ,INF, 8 ,INF,INF,INF],
    [INF,INF, 0 ,INF, 9 , 1 ,INF],
    [INF,INF,INF, 0 ,INF,INF, 3 ],
    [INF,INF,INF, 2 , 0 ,INF,INF],
    [INF,INF,INF,INF,INF, 0 , 2 ],
    [INF,INF,INF,INF,INF,INF, 0 ]
]

dijkstra(graph)