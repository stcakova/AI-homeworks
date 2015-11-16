import heapq

class Node(object):
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.dist= 0
        selfendDist= 0
        self.heuristics= 0

class AStar(object):
    def __init__(self):
        self.not_visited = []
        heapq.heapify(self.not_visited)
        self.visited = set()
        self.Nodes = []
        self.height = 6
        self.width = 6

    def init_grid(self):
        walls = ((0,5), (1,0), (1,1), (1, 3), (2, 4), (3,3), (4,3))
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) in walls:
                    reachable = False
                else:
                    reachable = True
                self.Nodes.append(Node(x, y, reachable))
        self.start = self.get_Node(0, 0)
        self.end = self.get_Node(5, 5)

    def get_heuristic(self, Node):
        return 10 * (abs(Node.x - self.end.x) + abs(Node.y - self.end.y))

    def get_Node(self, x, y):
        return self.Nodes[x * self.height + y]

    def neighbours(self, Node):
        Nodes = []
        if Node.x < self.width-1:
            Nodes.append(self.get_Node(Node.x+1, Node.y))
        if Node.y > 0:
            Nodes.append(self.get_Node(Node.x, Node.y-1))
        if Node.x > 0:
            Nodes.append(self.get_Node(Node.x-1, Node.y))
        if Node.y < self.height-1:
            Nodes.append(self.get_Node(Node.x, Node.y+1))
        return Nodes

    def display_path(self):
        Node = self.end
        while Node.parent is not self.start:
            Node = Node.parent
            print 'path:%d,%d' % (Node.x, Node.y)

    def update_Node(self, adj, Node):
        adj.dist= Node.dist + 10
        adjendDist= self.get_heuristic(adj)
        adj.parent = Node
        adj.heuristics= adjendDist+ adj.dist


    def process(self):
        heapq.heappush(self.not_visited, (self.start.heuristics, self.start))
        while len(self.not_visited):
            f, Node = heapq.heappop(self.not_visited)
            self.visited.add(Node)
            if Node is self.end:
                self.display_path()
                break
            adj_Nodes = self.neighbours(Node)
            for adj_Node in adj_Nodes:
                if adj_Node.reachable and adj_Node not in self.visited:
                    if (adj_Node.heuristics, adj_Node) in self.not_visited:
                        if adj_Node.dist > Node.dist+ 10:
                            self.update_Node(adj_Node, Node)
                    else:
                        self.update_Node(adj_Node, Node)
                        heapq.heappush(self.not_visited, (adj_Node.heuristics, adj_Node))


k = AStar()
k.init_grid()
k.process()

#sample maze
# S \ \ \ \ # 
# # # . # \ \
# . . . . # \
# . . . # . \
# . . . # . \
# . . . . . E


