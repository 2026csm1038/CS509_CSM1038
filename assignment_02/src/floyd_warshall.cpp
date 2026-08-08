#include "floyd_warshall.h"

#include <limits>

FloydWarshallResult floydWarshall(
    const vector<vector<long double>>& graph)
{
    const long double INF =
        numeric_limits<long double>::infinity();

    int V = graph.size();

    FloydWarshallResult result;
    result.distance = graph;
    result.hasNegativeCycle = false;

    for (int k = 0; k < V; k++)
    {
        for (int i = 0; i < V; i++)
        {
            if (result.distance[i][k] == INF)
            {
                continue;
            }

            for (int j = 0; j < V; j++)
            {
                if (result.distance[k][j] == INF)
                {
                    continue;
                }

                long double newDistance =
                    result.distance[i][k] +
                    result.distance[k][j];

                if (newDistance < result.distance[i][j])
                {
                    result.distance[i][j] = newDistance;
                }
            }
        }
    }

    for (int i = 0; i < V; i++)
    {
        if (result.distance[i][i] < 0)
        {
            result.hasNegativeCycle = true;
            break;
        }
    }

    return result;
}
