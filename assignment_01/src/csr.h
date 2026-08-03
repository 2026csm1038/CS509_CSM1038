#ifndef CSR_H
#define CSR_H

#include <vector>
#include <utility>
using namespace std;

struct CSRGraph{
  vector<double> values;
  vector<int> col_ind;
  vector<int> row_ptr;
  int V,E;
};

CSRGraph CSRconversion(const vector<vector<pair<int,double>>>& adjList,int V, int E);

#endif
