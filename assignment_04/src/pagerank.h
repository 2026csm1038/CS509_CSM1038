#ifndef PAGERANK_H
#define PAGERANK_H

#include <vector>
#include "../../common/csr.h"

using namespace std;

struct PageRankResult
{
    vector<double> ranks;
    int iterations;
    bool converged;
};

// Returns:
//   PageRank values for all vertices, number of iterations performed,
//   and whether the algorithm converged.
PageRankResult pageRank(const CSRGraph& graph,
                        double damping,
                        double tolerance,
                        int maxIterations);

#endif
