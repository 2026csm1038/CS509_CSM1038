#include "csr.h"

CSRGraph CSRconversion(const vector<vector<pair<int,double>>>& adjList,int V, int E){
   CSRGraph graph;
   graph.V = V;
   graph.E = E;

   graph.row_ptr.resize(V+1,0);

   for(int u=0;u<V;u++){
     graph.row_ptr[u+1] = graph.row_ptr[u] + (int)adjList[u].size();
   }

   int totalEdges = graph.row_ptr[V];
   graph.col_ind.resize(totalEdges);
   graph.values.resize(totalEdges);
  

   for(int u=0;u<V;u++){
     int start = graph.row_ptr[u];
     for(size_t i=0;i<adjList[u].size();i++){
        graph.col_ind[start + i] = adjList[u][i].first;
        graph.values[start + i]  = adjList[u][i].second;
     } 
   }
   return graph;
}
