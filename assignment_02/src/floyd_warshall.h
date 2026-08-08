#ifndef FLOYD_WARSHALL_H
#define FLOYD_WARSHALL_H

#include <vector>

using namespace std;

struct FloydWarshallResult
{
    vector<vector<long double>> distance;
    bool hasNegativeCycle;
};

FloydWarshallResult floydWarshall(
    const vector<vector<long double>>& graph);

#endif
