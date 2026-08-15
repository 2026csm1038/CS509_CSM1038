#include "mst.h"

#include <algorithm>
#include <functional>
#include <queue>
#include <tuple>
#include <numeric>

using namespace std;



// Disjoint Set Union for Kruskal


class DisjointSet
{
private:
    vector<int> parent;
    vector<int> rankValue;

public:
    explicit DisjointSet(int n)
    {
        parent.resize(n);
        rankValue.assign(n, 0);

        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x)
    {
        if (parent[x] != x)
        {
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    bool unite(int a, int b)
    {
        a = find(a);
        b = find(b);

        if (a == b)
        {
            return false;
        }

        if (rankValue[a] < rankValue[b])
        {
            swap(a, b);
        }

        parent[b] = a;

        if (rankValue[a] == rankValue[b])
        {
            rankValue[a]++;
        }

        return true;
    }
};


// Kruskal


MSTResult kruskalMST(const CSRGraph& graph)
{
    MSTResult result;

    result.totalWeight = 0.0L;
    result.connected = false;

    int V = graph.V;

    if (V <= 0)
    {
        result.connected = true;
        return result;
    }

    if (V == 1)
    {
        result.connected = true;
        return result;
    }

    struct Edge
    {
        int u;
        int v;
        long double weight;
    };

    vector<Edge> edges;

    //every edges appears twice so kept once 
    edges.reserve(graph.values.size() / 2);

    for (int u = 0; u < V; u++)
    {
        for (int index = graph.row_ptr[u];
             index < graph.row_ptr[u + 1];
             index++)
        {
            int v = graph.col_ind[index];

            if (u < v)
            {
                Edge edge;
                edge.u = u;
                edge.v = v;
                edge.weight = graph.values[index];

                edges.push_back(edge);
            }
        }
    }

    // Kruskal requires edges in non-decreasing weight order.
    sort(
        edges.begin(),
        edges.end(),
        [](const Edge& a, const Edge& b)
        {
            if (a.weight != b.weight)
            {
                return a.weight < b.weight;
            }

            if (a.u != b.u)
            {
                return a.u < b.u;
            }

            return a.v < b.v;
        }
    );

    DisjointSet dsu(V);

    for (const Edge& edge : edges)
    {
        if (dsu.unite(edge.u, edge.v))
        {
            MSTEdge selected;

            selected.u = edge.u;
            selected.v = edge.v;
            selected.weight = edge.weight;

            result.edges.push_back(selected);
            result.totalWeight += edge.weight;

            if (static_cast<int>(result.edges.size()) == V - 1)
            {
                break;
            }
        }
    }

    result.connected =
        (static_cast<int>(result.edges.size()) == V - 1);

    return result;
}


// Prims


MSTResult primMST(const CSRGraph& graph)
{
    MSTResult result;

    result.totalWeight = 0.0L;
    result.connected = false;

    int V = graph.V;

    if (V <= 0)
    {
        result.connected = true;
        return result;
    }

    if (V == 1)
    {
        result.connected = true;
        return result;
    }

    vector<bool> visited(V, false);

    /*
     * priority_queue stores:
     *
     * weight, vertex, parent
     *
     * greater<> makes it a min-priority queue.
     */
    using QueueEntry =
        tuple<long double, int, int>;

    priority_queue<
        QueueEntry,
        vector<QueueEntry>,
        greater<QueueEntry>
    > minHeap;

    
    minHeap.push({0.0L, 0, -1});

    while (!minHeap.empty())
    {
        auto [weight, vertex, parent] = minHeap.top();
        minHeap.pop();

        if (visited[vertex])
        {
            continue;
        }

        visited[vertex] = true;

        //The first vertex has parent -1 and does not contribute an edge to the MST.
        
        if (parent != -1)
        {
            MSTEdge selected;

            selected.u = parent;
            selected.v = vertex;
            selected.weight = weight;

            result.edges.push_back(selected);
            result.totalWeight += weight;
        }

        // Add all outgoing edges to unvisited neighbours
        for (int index = graph.row_ptr[vertex];
             index < graph.row_ptr[vertex + 1];
             index++)
        {
            int neighbour = graph.col_ind[index];
            long double edgeWeight =
                graph.values[index];

            if (!visited[neighbour])
            {
                minHeap.push(
                    {edgeWeight, neighbour, vertex}
                );
            }
        }

        if (static_cast<int>(result.edges.size()) == V - 1)
        {
            break;
        }
    }

    result.connected =
        (static_cast<int>(result.edges.size()) == V - 1);

    return result;
}
