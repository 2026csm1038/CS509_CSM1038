#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <utility>
#include <vector>

#include "bellman_ford.h"
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

    for (int u = 0; u < V; u++)
    {
        int vertex;
        int degree;

        inputFile >> vertex >> degree;

        if (vertex != u || degree < 0)
        {
            cerr << "Error: Invalid adjacency-list format." << endl;
            return 1;
        }

        for (int j = 0; j < degree; j++)
        {
            int v;
            double weight;

            inputFile >> v >> weight;

            if (v < 0 || v >= V)
            {
                cerr << "Error: Invalid destination vertex." << endl;
                return 1;
            }

            adjList[u].push_back({v, weight});
        }
    }

    string sourceLabel;
    int source;

    inputFile >> sourceLabel >> source;

    if (sourceLabel != "SOURCE")
    {
        cerr << "Error: Missing SOURCE declaration." << endl;
        return 1;
    }

    if (source < 0 || source >= V)
    {
        cerr << "Error: Invalid source vertex." << endl;
        return 1;
    }

    inputFile.close();

    // CSR conversion is outside the timed section.
    CSRGraph graph = CSRconversion(adjList, V, E);

    auto start = chrono::high_resolution_clock::now();

    BellmanFordResult result = bellmanFord(graph, source);

    auto stop = chrono::high_resolution_clock::now();

    auto elapsed =
        chrono::duration_cast<chrono::microseconds>(
            stop - start);

    cout << "Algorithm: Bellman-Ford" << endl;
    cout << "Source: " << source << endl;

    if (result.hasNegativeCycle)
    {
        cout << "Negative cycle: Yes" << endl;
    }
    else
    {
        cout << "Vertex Distance" << endl;

        const long double INF =
            numeric_limits<long double>::infinity();

        for (int v = 0; v < V; v++)
        {
            cout << v << " ";

            if (result.distance[v] == INF)
            {
                cout << "INF";
            }
            else
            {
                cout << fixed << setprecision(2)
                     << result.distance[v];
            }

            cout << endl;
        }

        cout << "Negative cycle: No" << endl;
    }

    cout << "Execution time: "
         << elapsed.count()
         << " microseconds" << endl;

    return 0;
}
