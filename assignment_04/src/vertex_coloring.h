#ifndef VERTEX_COLORING_H
#define VERTEX_COLORING_H

#include <vector>

#include "../../common/csr.h"

using namespace std;

struct VertexColoringResult
{
    vector<int> colors;
    int colorsUsed;
};

// The input graph is assumed to be valid and contain no self-loops.
VertexColoringResult greedyVertexColoring(const CSRGraph& graph);

#endif
