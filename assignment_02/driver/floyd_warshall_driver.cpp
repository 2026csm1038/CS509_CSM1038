#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

#include "floyd_warshall.h"

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

    int V;
    inputFile >> V;

    if (V <= 0)
    {
        cerr << "Invalid number of vertices." << endl;
        return 1;
    }

    const long double INF =
        numeric_limits<long double>::infinity();

    vector<vector<long double>> graph(
        V, vector<long double>(V, INF));

    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            string value;
            inputFile >> value;

            if (value == "INF")
            {
                graph[i][j] = INF;
            }
            else
            {
                graph[i][j] = stold(value);
            }
        }
    }

    inputFile.close();

  
    auto start = chrono::high_resolution_clock::now();

    FloydWarshallResult result = floydWarshall(graph);

    auto stop = chrono::high_resolution_clock::now();

    auto elapsed =
        chrono::duration_cast<chrono::milliseconds>(
            stop - start);

    if (result.hasNegativeCycle)
    {
        cout << "Negative weight cycle detected." << endl;
    }
    else
    {
        cout << "Shortest Distance Matrix:" << endl;

        for (int i = 0; i < V; i++)
        {
            for (int j = 0; j < V; j++)
            {
                if (result.distance[i][j] == INF)
                {
                    cout << "INF";
                }
                else
                {
                    cout << fixed << setprecision(2)
                         << static_cast<double>(
                                result.distance[i][j]);
                }

                if (j < V - 1)
                {
                    cout << " ";
                }
            }

            cout << endl;
        }
    }

    cout << "\nExecution Time : "
         << elapsed.count()
         << " ms" << endl;

    return 0;
}
