#include "vertex_coloring.h"

#include <vector>

using namespace std;

VertexColoringResult greedyVertexColoring(const CSRGraph& graph)
{
    VertexColoringResult result;

    int V = graph.V;

    result.colors.assign(V, -1);
    result.colorsUsed = 0;

    vector<bool> usedColors(V, false);

    for (int u = 0; u < V; u++)
    {
        // Mark colors used by already-colored neighbours.
        for (int idx = graph.row_ptr[u];
             idx < graph.row_ptr[u + 1];
             idx++)
        {
            int v = graph.col_ind[idx];

            if (v >= 0 && v < V && result.colors[v] != -1)
            {
                usedColors[result.colors[v]] = true;
            }
        }

        // Find the smallest available color.
        int color = 0;

        while (color < V && usedColors[color])
        {
            color++;
        }

        result.colors[u] = color;

        if (color + 1 > result.colorsUsed)
        {
            result.colorsUsed = color + 1;
        }

        // Reset only the colors that could have been marked.
        for (int idx = graph.row_ptr[u];
             idx < graph.row_ptr[u + 1];
             idx++)
        {
            int v = graph.col_ind[idx];

            if (v >= 0 && v < V && result.colors[v] != -1)
            {
                usedColors[result.colors[v]] = false;
            }
        }
    }

    return result;
}
