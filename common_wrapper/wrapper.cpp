#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

void showMenu() {
    cout << "\n===================================\n";
    cout << "   CS509_2026CSM1038(INDIVIDUAL) Common Wrapper - Menu\n";
    cout << "===================================\n";
    cout << "1. GEMM (Simple + Blocking)\n";
    cout << "2. CSR Conversion Test\n";
    cout << "0. Exit\n";
    cout << "-----------------------------------\n";
    cout << "Enter choice: ";
}

void runGemm() {
    string filename;
    cout << "Enter path to GEMM test file (e.g. assignment_01/tests/gemm_test_01.txt): ";
    cin >> filename;

    string command = "./assignment_01/driver/gemm_driver " + filename;
    cout << "\nRunning: " << command << "\n\n";
    int result = system(command.c_str());

    if (result != 0) {
        cerr << "Error: GEMM driver exited with a non-zero status.\n";
    }
}

void runCsr() {
    string filename;
    cout << "Enter path to CSR test file (e.g. assignment_01/tests/csr_test_04.txt): ";
    cin >> filename;

    string command = "./assignment_01/tests/csr_test " + filename;
    cout << "\nRunning: " << command << "\n\n";
    int result = system(command.c_str());

    if (result != 0) {
        cerr << "Error: CSR test exited with a non-zero status.\n";
    }
}

int main() {
    int choice;

    do {
        showMenu();
        cin >> choice;

        switch (choice) {
            case 1:
                runGemm();
                break;
            case 2:
                runCsr();
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
