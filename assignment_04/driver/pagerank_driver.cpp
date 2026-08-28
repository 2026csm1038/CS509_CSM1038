#include <chrono>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

#include "../src/pagerank.h"
#include "../../common/csr.h"

using namespace std;
using namespace chrono;

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        cerr << "Usage: " << argv[0]
             << " <input_file>" << endl;
        return 1;
    }

    string inputFile = argv[1];

    ifstream fin(inputFile);

    if (!fin)
    {
        cerr << "Error: Cannot open input file: "
             << inputFile << endl;
        return 1;
    }

    int V, E;

    if (!(fin >> V >> E))
    {
        cerr << "Error: Invalid graph header." << endl;
        return 1;
    }

    if (V <= 0)
    {
        cerr << "Error: Number of vertices must be positive."
             << endl;
        return 1;
    }

    if (E < 0)
    {
        cerr << "Error: Number of edges cannot be negative."
             << endl;
        return 1;
    }

    vector<vector<pair<int, double>>> adjacency(V);

    fin.ignore(numeric_limits<streamsize>::max(), '\n');

    string line;

    for (int u = 0; u < V; u++)
    {
        if (!getline(fin, line))
        {
            cerr << "Error: Missing adjacency list for vertex "
                 << u << endl;
            return 1;
        }

        stringstream ss(line);

        int vertex;

        if (!(ss >> vertex))
        {
            cerr << "Error: Invalid adjacency list for vertex "
                 << u << endl;
            return 1;
        }

        if (vertex != u)
        {
            cerr << "Error: Expected vertex " << u
                 << " but found " << vertex << endl;
            return 1;
        }

        int neighbour;

        while (ss >> neighbour)
        {
            if (neighbour < 0 || neighbour >= V)
            {
                cerr << "Error: Invalid neighbour " << neighbour
                     << " for vertex " << u << endl;
                return 1;
            }

            adjacency[u].push_back({neighbour, 1.0});
        }
    }

    double damping;
    double tolerance;
    int maxIterations;

    string keyword;

    if (!(fin >> keyword >> damping))
    {
        cerr << "Error: Missing DAMPING parameter." << endl;
        return 1;
    }

    if (keyword != "DAMPING")
    {
        cerr << "Error: Expected DAMPING parameter." << endl;
        return 1;
    }

    if (!(fin >> keyword >> tolerance))
    {
        cerr << "Error: Missing TOLERANCE parameter." << endl;
        return 1;
    }

    if (keyword != "TOLERANCE")
    {
        cerr << "Error: Expected TOLERANCE parameter." << endl;
        return 1;
    }

    if (!(fin >> keyword >> maxIterations))
    {
        cerr << "Error: Missing MAX_ITERATIONS parameter."
             << endl;
        return 1;
    }

    if (keyword != "MAX_ITERATIONS")
    {
        cerr << "Error: Expected MAX_ITERATIONS parameter."
             << endl;
        return 1;
    }

    
     // Validate PageRank parameters.
     
    if (damping < 0.0 || damping > 1.0)
    {
        cerr << "Error: Damping factor must be between 0 and 1."
             << endl;
        return 1;
    }

    if (tolerance <= 0.0)
    {
        cerr << "Error: Tolerance must be positive." << endl;
        return 1;
    }

    if (maxIterations <= 0)
    {
        cerr << "Error: Maximum iterations must be positive."
             << endl;
        return 1;
    }

    
    CSRGraph graph = CSRconversion(adjacency, V, E);

    
    auto start = high_resolution_clock::now();

    PageRankResult result =
        pageRank(graph,
                 damping,
                 tolerance,
                 maxIterations);

    auto end = high_resolution_clock::now();

    double executionTime =
        duration<double, milli>(end - start).count();

    cout << fixed << setprecision(10);

    cout << "Algorithm: PageRank" << endl;
    cout << "Vertices: " << V << endl;
    cout << "Edges: " << E << endl;
    cout << "Damping: " << damping << endl;
    cout << "Tolerance: " << tolerance << endl;
    cout << "Max iterations: " << maxIterations << endl;

    cout << "Vertex ranks:" << endl;

    double rankSum = 0.0;

    for (int i = 0; i < V; i++)
    {
        cout << i << " " << result.ranks[i] << endl;
        rankSum += result.ranks[i];
    }

    cout << "Sum of ranks: " << rankSum << endl;
    cout << "Iterations: " << result.iterations << endl;
    cout << "Converged: "
         << (result.converged ? "true" : "false")
         << endl;

    cout << "Execution time: "
         << executionTime
         << " ms" << endl;

    return 0;
}
