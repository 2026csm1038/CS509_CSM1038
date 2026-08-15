#ifndef MST_H
#define MST_H

#include <vector>
#include "csr.h"

using namespace std;

struct MSTEdge
{
    int u;
    int v;
    long double weight;
};

struct MSTResult
{
    vector<MSTEdge> edges;
    long double totalWeight;
    bool connected;
};

// Kruskal
MSTResult kruskalMST(const CSRGraph& graph);

// Prims
MSTResult primMST(const CSRGraph& graph);

#endif
