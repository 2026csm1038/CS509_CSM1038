#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

#include "../src/vertex_coloring.h"
#include "../../common/csr.h"

using namespace std;
using namespace chrono;

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }

    string filename = argv[1];

    ifstream fin(filename);

    if (!fin)
    {
        cerr << "Error: Cannot open input file: "
             << filename << endl;
        return 1;
    }

    int V, E;

    if (!(fin >> V >> E))
    {
        cerr << "Error: Invalid input file." << endl;
        return 1;
    }

    if (V <= 0 || E < 0)
    {
        cerr << "Error: Invalid number of vertices or edges." << endl;
        return 1;
    }

    vector<vector<pair<int, double>>> adjacency(V);

    for (int u = 0; u < V; u++)
    {
        int vertex;
        int degree;

        if (!(fin >> vertex >> degree))
        {
            cerr << "Error: Invalid adjacency-list format at vertex "
                 << u << "." << endl;
            return 1;
        }

        if (vertex != u)
        {
            cerr << "Error: Vertex numbering mismatch at vertex "
                 << u << "." << endl;
            return 1;
        }

        if (degree < 0)
        {
            cerr << "Error: Invalid degree at vertex "
                 << u << "." << endl;
            return 1;
        }

        for (int j = 0; j < degree; j++)
        {
            int v;

            if (!(fin >> v))
            {
                cerr << "Error: Missing neighbour for vertex "
                     << u << "." << endl;
                return 1;
            }

            if (v < 0 || v >= V)
            {
                cerr << "Error: Invalid neighbour "
                     << v << " for vertex " << u << "." << endl;
                return 1;
            }

            if (v == u)
            {
                cerr << "Error: Self-loop detected at vertex "
                     << u << "." << endl;
                return 1;
            }

            adjacency[u].push_back({v, 1.0});
        }
    }

    /*
     * CSR conversion is preprocessing.
     * It is intentionally outside the timed region.
     */
    CSRGraph graph = CSRconversion(adjacency, V, E);

    /*
     * Only the actual greedy coloring algorithm is timed.
     */
    auto start = high_resolution_clock::now();

    VertexColoringResult result =
        greedyVertexColoring(graph);

    auto end = high_resolution_clock::now();

    double executionTime =
        duration<double, milli>(end - start).count();

    cout << "Algorithm: Greedy Vertex Coloring" << endl;
    cout << "Vertices: " << V << endl;
    cout << "Edges: " << E << endl;

    cout << "Vertex colors:" << endl;

    for (int i = 0; i < V; i++)
    {
        cout << i << " " << result.colors[i] << endl;
    }

    cout << "Colors used: "
         << result.colorsUsed << endl;

    cout << "Execution time: "
         << executionTime << " ms" << endl;

    return 0;
}
