#include <algorithm>
#include "gemm.h"


int chooseBlockSize(int M, int K, int N) {
    int minDim = min({M, K, N});

    int block = 8;
    while (block * 2 <= minDim && block * 2 <= 64) {
        block *= 2;
    }
    return block;
}

vector<vector<double>> Simple(const vector<vector<double>>& A,const vector<vector<double>>& B,int M,int K,int N){
  
  vector<vector<double>> C(M,vector<double>(N,0.0));
  for(int i=0;i<M;i++){
     for(int j=0;j<N;j++){
       double sum = 0.0;
       for(int k=0;k<K;k++){
          sum += A[i][k] * B[k][j];
    
       }     
       C[i][j] = sum;
     }

  }
  return C;

}

vector<vector<double>> Blocking(const vector<vector<double>>& A,const vector<vector<double>>& B, int M,int K,int N,int blockSize){

  vector<vector<double>> C(M,vector<double>(N,0.0));
  for(int i=0;i<M;i+=blockSize){
      for(int j=0;j<N;j+=blockSize){
         for(int k=0;k<K;k+=blockSize){
            int iMax = min(i+blockSize,M);
            int jMax = min(j+blockSize,N);
            int kMax = min(k+blockSize,K);
           
            for(int x=i;x<iMax;x++){
                for(int y=j;y<jMax;y++){
                    double sum = 0.0;
                    for(int z=k;z<kMax;z++){
                      sum +=A[x][z]*B[z][y];
                    }
                    C[x][y] = sum;
                }
            }
         }
      }
  }
  return C;
}
