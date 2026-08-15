#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <iomanip>
#include <chrono>

#include "mst.h"
#include "csr.h"

using namespace std;

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }

    ifstream inputFile(argv[1]);

    if (!inputFile)
    {
        cerr << "Error: Unable to open input file." << endl;
        return 1;
    }

    int V, E;
    inputFile >> V >> E;

    if (V <= 0 || E < 0)
    {
        cerr << "Error: Invalid graph size." << endl;
        return 1;
    }

    vector<vector<pair<int, double>>> adjList(V);

    /*
        Input format:

        V E
        u v weight
        u v weight
        ...

        The graph is undirected, so every edge is
        stored in both directions.
    */

    for (int i = 0; i < E; i++)
    {
        int u, v;
        double weight;

        inputFile >> u >> v >> weight;

        if (u < 0 || u >= V || v < 0 || v >= V)
        {
            cerr << "Error: Invalid vertex number." << endl;
            return 1;
        }

        adjList[u].push_back({v, weight});
        adjList[v].push_back({u, weight});
    }

    inputFile.close();

    /*
        Convert adjacency list to CSR.
        CSR conversion is kept outside the timing section.
    */
    CSRGraph graph = CSRconversion(adjList, V, 2 * E);

    cout << fixed << setprecision(2);

    // --------------------------------------------------
    // Prim's Algorithm
    // --------------------------------------------------

    auto primStart = chrono::high_resolution_clock::now();

    MSTResult primResult = primMST(graph);

    auto primStop = chrono::high_resolution_clock::now();

    auto primTime =
        chrono::duration_cast<chrono::microseconds>(
            primStop - primStart);

    cout << "\n========================================" << endl;
    cout << "Prim's MST" << endl;
    cout << "========================================" << endl;

    if (!primResult.connected)
    {
        cout << "Graph is disconnected." << endl;
        cout << "MST does not exist." << endl;
    }
    else
    {
        cout << "Edges in MST: "
             << primResult.edges.size()
             << endl;

        cout << "Total MST Weight: "
             << primResult.totalWeight
             << endl;

        cout << "MST Edges:" << endl;

        for (const MSTEdge& edge : primResult.edges)
        {
            cout << edge.u << " "
                 << edge.v << " "
                 << edge.weight << endl;
        }
    }

    cout << "Execution Time: "
         << primTime.count()
         << " microseconds"
         << endl;


    // --------------------------------------------------
    // Kruskal's Algorithm
    // --------------------------------------------------

    auto kruskalStart = chrono::high_resolution_clock::now();

    MSTResult kruskalResult = kruskalMST(graph);

    auto kruskalStop = chrono::high_resolution_clock::now();

    auto kruskalTime =
        chrono::duration_cast<chrono::microseconds>(
            kruskalStop - kruskalStart);

    cout << "\n========================================" << endl;
    cout << "Kruskal's MST" << endl;
    cout << "========================================" << endl;

    if (!kruskalResult.connected)
    {
        cout << "Graph is disconnected." << endl;
        cout << "MST does not exist." << endl;
    }
    else
    {
        cout << "Edges in MST: "
             << kruskalResult.edges.size()
             << endl;

        cout << "Total MST Weight: "
             << kruskalResult.totalWeight
             << endl;

        cout << "MST Edges:" << endl;

        for (const MSTEdge& edge : kruskalResult.edges)
        {
            cout << edge.u << " "
                 << edge.v << " "
                 << edge.weight << endl;
        }
    }

    cout << "Execution Time: "
         << kruskalTime.count()
         << " microseconds"
         << endl;

    return 0;
}
