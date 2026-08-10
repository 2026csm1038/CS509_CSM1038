
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

void showMenu()
{
    cout << "\n===================================\n";
    cout << "   CS509_CSM1038 (INDIVIDUAL) Common Wrapper\n";
    cout << "===================================\n";
    cout << "1. GEMM (Simple + Blocking)\n";
    cout << "2. CSR Conversion Test\n";
    cout << "3. Bellman-Ford\n";
    cout << "4. Floyd-Warshall\n";
    cout << "0. Exit\n";
    cout << "-----------------------------------\n";
    cout << "Enter choice: ";
}

void runGemm()
{
    string filename;

    cout << "Enter path to GEMM test file "
         << "(e.g. assignment_01/tests/gemm_test_01.txt): ";
    cin >> filename;

    string command =
        "./assignment_01/driver/gemm_driver " + filename;

    cout << "\nRunning: " << command << "\n\n";

    int result = system(command.c_str());

    if (result != 0)
    {
        cerr << "Error: GEMM driver exited with a non-zero status.\n";
    }
}

void runCsr()
{
    string filename;

    cout << "Enter path to CSR test file "
         << "(e.g. assignment_01/tests/csr_test_04.txt): ";
    cin >> filename;

    string command =
        "./assignment_01/tests/csr_test " + filename;

    cout << "\nRunning: " << command << "\n\n";

    int result = system(command.c_str());

    if (result != 0)
    {
        cerr << "Error: CSR test exited with a non-zero status.\n";
    }
}

void runBellmanFord()
{
    string filename;

    cout << "Enter path to Bellman-Ford test file "
         << "(e.g. assignment_02/tests/bellman_ford/bf_10.txt): ";
    cin >> filename;

    string command =
        "./assignment_02/driver/bellman_ford_driver " + filename;

    cout << "\nRunning: " << command << "\n\n";

    int result = system(command.c_str());

    if (result != 0)
    {
        cerr << "Error: Bellman-Ford driver exited with a non-zero status.\n";
    }
}

void runFloydWarshall()
{
    string filename;

    cout << "Enter path to Floyd-Warshall test file "
         << "(e.g. assignment_02/tests/floyd_warshall/fw_10.txt): ";
    cin >> filename;

    string command =
        "./assignment_02/driver/floyd_warshall_driver " + filename;

    cout << "\nRunning: " << command << "\n\n";

    int result = system(command.c_str());

    if (result != 0)
    {
        cerr << "Error: Floyd-Warshall driver exited with a non-zero status.\n";
    }
}

int main()
{
    int choice;

    do
    {
        showMenu();
        cin >> choice;

        switch (choice)
        {
            case 1:
                runGemm();
                break;

            case 2:
                runCsr();
                break;

            case 3:
                runBellmanFord();
                break;

            case 4:
                runFloydWarshall();
                break;

            case 0:
                cout << "Exiting.\n";
                break;

            default:
                cout << "Invalid choice. Please try again.\n";
        }

    } while (choice != 0);

    return 0;
}

