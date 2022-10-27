#include <iostream>
#include <vector>
using namespace std;

void print(int numbers[], int n){
    for(int i = 0; i < n; i++){
        cout << numbers[i] << endl;
    }    
}

void printPointer(int* numbers, int n){
    for(int i = 0; i < n; i++){
        cout << *numbers <<endl;
        numbers++;
    }
}

void printVector(vector<int> &numbers){
    numbers[0] = 99;
    for(int i = 0; i < numbers.size(); i++){
        cout << numbers[i] << endl;    
    }
}

int main(){
    int x;
    //cin >> x;
    cout << "Hola mundo: " << x;

    int numbers[] = {1, 2, 3, 4};
    vector<int> values = {1, 2, 3, 4};
    print(numbers, sizeof(numbers)/sizeof(int));
    printPointer(numbers, sizeof(numbers)/sizeof(int));
    printVector(values);
    cout << values[0] << endl;
    return 0;
}