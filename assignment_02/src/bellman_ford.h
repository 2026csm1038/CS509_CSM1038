#ifndef BELLMAN_FORD_H
#define BELLMAN_FORD_H

#include <vector>
#include "csr.h"

using namespace std;


struct BellmanFordResult
{
    vector<long double> distance;
    bool hasNegativeCycle;
};

BellmanFordResult bellmanFord(const CSRGraph &graph, int source);

#endif
