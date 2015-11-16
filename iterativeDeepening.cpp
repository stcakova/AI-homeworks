#include <iostream>
#include<queue>
#include<stack>
using namespace std;

bool visited[6] = { 0, 0, 0, 0, 0, 0 };
bool graph[6][6] = { { 0, 1, 1, 1, 0, 0 }, { 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 1, 0 },
{ 0, 0, 0, 0, 0, 1 }, { 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 1, 0 } };

bool DLS(int start, int end, int depth) {
	if (start == end)
		return true;
	if (depth == 0)
		return false;
	if (start != end)
		visited[start] = true;
	for (int i = 0; i < 6; i++)
	{
		if (graph[start][i] == 1 && !visited[i])
			if (DLS(i, end, depth - 1))
				return true;
	}
	return false;
}

bool IterativeDeepening(int start, int end) {
	for (int i = 0; i < 6; i++)
	{
		if (DLS(start,end,i))
		{
			return true;
		}
	}
	return false;
}
int main()
{
  bool graph[6][6] = { { 0, 1, 1, 1, 0, 0 }, { 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 1, 0 },
  { 0, 0, 0, 0, 0, 1 }, { 0, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 1, 0 } };
	cout << "path between verteces 0 and 4 " << (dls(0, 4, 1) ? "exists" : "doesn't exist") << endl;  //bfs should return 1. the is path between verteces 0 and 5
	cout << "path between verteces 4 and 5 " << (bfszgraph, 4, 5) ? "exists" : "doesn't exist") << endl;	// bfs should return 0. the is no path between verteces 0 and 5
	cout << "dfs : ";
	dfs(graph, 0); // prints all verteces from the graph 
	return 0;
}
