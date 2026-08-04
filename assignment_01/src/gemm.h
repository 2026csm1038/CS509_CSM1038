#ifndef GEMM_H
#define GEMM_H

#include <vector>
using namespace std;

vector<vector<double>> Simple(const vector<vector<double>>& A,const vector<vector<double>>& B,int M, int K, int N);
vector<vector<double>> Blocking(const vector<vector<double>>& A,const vector<vector<double>>& B,int M, int K, int N,int blockSize);

int chooseBlockSize(int M, int K, int N);// Picks a reasonable block size for gemmBlocking based on how big the
// matrices actually are, instead of using one fixed value for every
// test case.

#endif 
