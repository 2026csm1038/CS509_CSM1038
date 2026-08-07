#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

#include "bellman_ford.h"
#include "csr.h"

using namespace std;

int main(int argc, char *argv[])
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
        cerr << "Invalid graph size." << endl;
        return 1;
    }

    vector<vector<pair<int, double>>> adjList(V);

    for (int i = 0; i < E; i++)
    {
        int u, v;
        double w;

        inputFile >> u >> v >> w;

        if (u < 0 || u >= V || v < 0 || v >= V)
        {
            cerr << "Invalid edge encountered." << endl;
            return 1;
        }

        adjList[u].push_back({v, w});
    }

    int source;

    inputFile >> source;

    if (source < 0 || source >= V)
    {
        cerr << "Invalid source vertex." << endl;
        return 1;
    }

    inputFile.close();


    CSRGraph graph = CSRconversion(adjList, V, E);

    auto start = chrono::high_resolution_clock::now();

    BellmanFordResult result = bellmanFord(graph, source);

    auto stop = chrono::high_resolution_clock::now();

    auto elapsed =
        chrono::duration_cast<chrono::milliseconds>(stop - start);

    if (result.hasNegativeCycle)
    {
        cout << "Negative weight cycle detected." << endl;
    }
    else
    {
        cout << "Source Vertex : " << source << "\n\n";

        cout << left
        << setw(10) << "Vertex"
        << "Distance" << endl;

        for (int i = 0; i < V; i++)
        {
            cout << left << setw(10) << i;

            if (result.distance[i] ==
                numeric_limits<long double>::infinity())
            {
                cout << "INF";
            }
            else
            {
                cout << fixed << setprecision(2)
                     << static_cast<double>(result.distance[i]);
            }

            cout << endl;
        }
    }

    cout << "\nExecution Time : "
     << elapsed.count()
     << " ms" << endl;

    return 0;
}
