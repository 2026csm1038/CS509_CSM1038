#ifndef GEMM_H
#define GEMM_H

#include <vector>
using namespace std;

vector<vector<double>> Simple(const vector<vector<double>>& A,const vector<vector<double>>& B,int M, int K, int N);
vector<vector<double>> Blocking(const vector<vector<double>>& A,const vector<vector<double>>& B,int M, int K, int N,int blockSize);

int chooseBlockSize(int M, int K, int N);

#endif 
