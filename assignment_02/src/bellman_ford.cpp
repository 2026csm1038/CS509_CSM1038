#include "bellman_ford.h"

#include <limits>

BellmanFordResult bellmanFord(const CSRGraph &graph, int source)
{
    const long double INF = numeric_limits<long double>::infinity();

    BellmanFordResult result;
    result.distance.assign(graph.V, INF);
    result.hasNegativeCycle = false;

    if (source < 0 || source >= graph.V)
    {
        return result;
    }

    result.distance[source] = 0.0;

   
    for (int iteration = 1; iteration < graph.V; iteration++)
    {
        bool updated = false;

        for (int u = 0; u < graph.V; u++)
        {
            if (result.distance[u] == INF)
            {
                continue;
            }

            for (int edge = graph.row_ptr[u];
                 edge < graph.row_ptr[u + 1];
                 edge++)
            {
                int v = graph.col_ind[edge];
                long double weight =
                    static_cast<long double>(graph.values[edge]);

                if (result.distance[u] + weight < result.distance[v])
                {
                    result.distance[v] =
                        result.distance[u] + weight;

                    updated = true;
                }
            }
        }

        
        if (!updated)
        {
            break;
        }
    }

    for (int u = 0; u < graph.V; u++)
    {
        if (result.distance[u] == INF)
        {
            continue;
        }

        for (int edge = graph.row_ptr[u];
             edge < graph.row_ptr[u + 1];
             edge++)
        {
            int v = graph.col_ind[edge];
            long double weight =
                static_cast<long double>(graph.values[edge]);

            if (result.distance[u] + weight < result.distance[v])
            {
                result.hasNegativeCycle = true;
                return result;
            }
        }
    }

    return result;
}
