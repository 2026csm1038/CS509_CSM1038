#include "csr.h"

CSRGraph CSRconversion(const vector<vector<pair<int,double>>>& adjList,int V, int E){
   CSRGraph graph;
   graph.V = V;
   graph.E = E;

   graph.row_ptr.resize(V+1,0);

   for(int u=0;u<V;u++){
     graph.row_ptr[u+1] = graph.row_ptr[u] + (int)adjList[u].size();
   }// After this loop, row_ptr[u] tells us exactly where vertex u's
   // edges will start once we flatten everything into col_ind/values.

   int totalEdges = graph.row_ptr[V];// Total number of edges across all vertices
   graph.col_ind.resize(totalEdges);
   graph.values.resize(totalEdges);
  

   for(int u=0;u<V;u++){
     int start = graph.row_ptr[u];
     for(size_t i=0;i<adjList[u].size();i++){
        graph.col_ind[start + i] = adjList[u][i].first;// neighbor vertex
        graph.values[start + i]  = adjList[u][i].second;// edge weight
     } 
   }
   return graph;
}
