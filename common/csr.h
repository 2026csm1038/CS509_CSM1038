#ifndef CSR_H
#define CSR_H

#include <vector>
#include <utility>
using namespace std;

struct CSRGraph{
  vector<double> values;// edge weight
  vector<int> col_ind;// destination vertex of each edge
  vector<int> row_ptr;// each vertex's edges start/end

  int V,E;
};

CSRGraph CSRconversion(const vector<vector<pair<int,double>>>& adjList,int V, int E);// Converts an adjacency-list graph into CSR format

#endif
