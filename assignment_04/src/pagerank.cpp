#include "pagerank.h"

#include <cmath>
#include <numeric>

using namespace std;

PageRankResult pageRank(const CSRGraph& graph,
                        double damping,
                        double tolerance,
                        int maxIterations)
{
    int V = graph.V;

    PageRankResult result;
    result.ranks.assign(V, 0.0);
    result.iterations = 0;
    result.converged = false;

    if (V == 0)
    {
        result.converged = true;
        return result;
    }

   
     // Every vertex starts with equal rank.
     
    vector<double> rank(V, 1.0 / V);
    vector<double> newRank(V, 0.0);

    for (int iteration = 1; iteration <= maxIterations; iteration++)
    {
        
        double base = (1.0 - damping) / V;

        fill(newRank.begin(), newRank.end(), base);

        //Calculate the total rank belonging to dangling vertices  (vertices having no outgoing edges)
        double danglingRank = 0.0;

        for (int u = 0; u < V; u++)
        {
            int start = graph.row_ptr[u];
            int end = graph.row_ptr[u + 1];

            if (start == end)
            {
                danglingRank += rank[u];
            }
        }

         //Redistribute dangling-vertex rank equally among all vertices.
        double danglingContribution = damping * danglingRank / V;

        for (int v = 0; v < V; v++)
        {
            newRank[v] += danglingContribution;
        }

        // Distribute each vertex's rank equally among its outgoing neighbours
        for (int u = 0; u < V; u++)
        {
            int start = graph.row_ptr[u];
            int end = graph.row_ptr[u + 1];

            int outDegree = end - start;

            if (outDegree == 0)
            {
                continue;
            }

            double contribution =
                damping * rank[u] / outDegree;

            for (int idx = start; idx < end; idx++)
            {
                int v = graph.col_ind[idx];
                newRank[v] += contribution;
            }
        }

        
         // Calculate total change in PageRank.
         
        double difference = 0.0;

        for (int v = 0; v < V; v++)
        {
            difference += fabs(newRank[v] - rank[v]);
        }

        rank.swap(newRank);

        result.iterations = iteration;

        if (difference <= tolerance)
        {
            result.converged = true;
            break;
        }
    }

    
    double sum = accumulate(rank.begin(), rank.end(), 0.0);

    if (sum > 0.0)
    {
        for (double& value : rank)
        {
            value /= sum;
        }
    }

    result.ranks = rank;

    return result;
}
