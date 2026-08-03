#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include "../src/gemm.h"

using namespace std;
using namespace std::chrono;

void printMatrix(const vector<vector<double>>& C){
  for(const auto& row: C){
     for(size_t j=0;j<row.size();j++){
        cout<<row[j];
        if(j!=row.size()-1) cout<<" ";
     }
     cout<<"\n";
  }
}
int main(int argc, char* argv[]){
   if(argc < 2){
      cerr<<"ERROR:Input file not provided \n";
      cerr<<"Usage: "<<argv[0]<<"<gemm_test_file.txt> \n";
      return 1;
   }

  ifstream infile(argv[1]);
  if (!infile.is_open()) {
        cerr << "Error: Could not open input file: " << argv[1] << "\n";
        return 1;
    }
  int M,K,N;
  infile >>M>>K>>N;
  
  vector<vector<double>> A(M, vector<double>(K));
    for (int i = 0; i < M; i++)
        for (int j = 0; j < K; j++)
            infile >> A[i][j];

  vector<vector<double>> B(K, vector<double>(N));
    for (int i = 0; i < K; i++)
        for (int j = 0; j < N; j++)
            infile >> B[i][j];
 
  infile.close();

  auto start1 = high_resolution_clock::now();
  vector<vector<double>> C1 = Simple(A,B,M,K,N);
  auto end1 = high_resolution_clock::now();


    double timeSimple = duration<double, milli>(end1 - start1).count();

    cout << "Algorithm: GEMM Simple\n";
    cout << "Result matrix:\n";
    printMatrix(C1);
    cout << "Execution time: " << timeSimple << " ms\n\n";


    int blockSize = chooseBlockSize(M, K, N);
    auto start2 = high_resolution_clock::now();
    vector<vector<double>> C2 = Blocking(A, B, M, K, N, blockSize);
    auto end2 = high_resolution_clock::now();
    double timeBlocking = duration<double, milli>(end2 - start2).count();

    cout << "Algorithm: GEMM Blocking\n";
    cout << "Result matrix:\n";
    printMatrix(C2);
    cout << "Execution time: " << timeBlocking << " ms\n";

    return 0;
}
