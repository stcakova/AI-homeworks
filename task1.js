var visited = {},
  goalVertex = "082137645",
  queue = [];

function generateSingleVertex(vertex, position1, position2) {
  vertex = vertex.split('');
  var b = vertex[position1];
  vertex[position1] = vertex[position2];
  vertex[position2] = b;
  return vertex.join('');
}


function findNeighbours(vertex) {
  var index = vertex.indexOf("0");
  var allNeighbours = [],
    currentVertex;
  if (index + 1 < 9 && [2, 5].indexOf(index) === -1) {
    currentVertex = generateSingleVertex(vertex, index, index + 1);
    allNeighbours.push(currentVertex);
  }
  if (index + 3 < 9) {
    currentVertex = generateSingleVertex(vertex, index, index + 3);
    allNeighbours.push(currentVertex);
  }
  if (index - 1 >= 0 && [3, 6].indexOf(index) === -1) {
    currentVertex = generateSingleVertex(vertex, index, index - 1);
    allNeighbours.push(currentVertex);
  }
  if (index - 3 >= 0) {
    currentVertex = generateSingleVertex(vertex, index, index - 3);
    allNeighbours.push(currentVertex);
  }
  return allNeighbours;
}

function isVisited(vertex) { 		//hash : string ---> true || false
  return visited[vertex] ? true : false;
}

function bfs(matrix) {
  var startVertex = matrix.toString().replace(/,/g, '');
  visited[startVertex] = true;
  queue.push([startVertex,0])
  var result = bfsHelper(0, queue);
  return result;
}

function bfsHelper(numberOfIterations, queue) {
  while (queue.length > 0) {
    numberOfIterations++;
    var current = queue.shift();
    var vertex = current[0];
    var dist = current[1];
    if (vertex === goalVertex)
      return dist;

    var neighbours = findNeighbours(vertex);

    for (var i = 0; i < neighbours.length; i++) {
      if (!isVisited(neighbours[i])) {
        visited[neighbours[i]] = true;
        queue.push([neighbours[i],++dist]);
      }
    }
  }
}

var result = bfs([
  [6, 4, 8],
  [1, 2, 3],
  [5, 7, 0]
]);
console.log(result ? "Number of iterations : " + result :
  'State\n1 2 3\n4 5 6\n7 8 0\ncould not be reached!');
