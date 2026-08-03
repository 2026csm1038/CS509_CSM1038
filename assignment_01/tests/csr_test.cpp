#include <iostream>
#include <fstream>
#include <sstream>
#include "../src/csr.h"

using namespace std;

void printCSR(const CSRGraph& g) {
    cout << "V = " << g.V << ", E = " << g.E << "\n";

    cout << "row_ptr: ";
    for (int v : g.row_ptr) cout << v << " ";
    cout << "\n";

    cout << "col_idx: ";
    for (int v : g.col_ind) cout << v << " ";
    cout << "\n";

    cout << "values: ";
    for (double v : g.values) cout << v << " ";
    cout << "\n";
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " <adjacency_list_file.txt>\n";
        return 1;
    }

    ifstream infile(argv[1]);
    if (!infile.is_open()) {
        cerr << "Error: could not open file: " << argv[1] << "\n";
        return 1;
    }

    int V, E;
    infile >> V >> E;

    vector<vector<pair<int, double>>> adjList(V);

    for (int i = 0; i < V; i++) {
        int u, degree;
        infile >> u >> degree;
        for (int d = 0; d < degree; d++) {
            int neighbor;
            infile >> neighbor;
            adjList[u].push_back({neighbor, 1.0}); // unweighted -> weight 1.0
        }
    }

    // Optionally read (and ignore) the SOURCE line if present
    string tag;
    if (infile >> tag) {
        int source;
        infile >> source;
        // not used for CSR conversion itself
    }

    infile.close();

    CSRGraph graph = CSRconversion(adjList, V, E);
    cout << "File: " << argv[1] << "\n";
    printCSR(graph);
    cout << "\n";

    return 0;
}
