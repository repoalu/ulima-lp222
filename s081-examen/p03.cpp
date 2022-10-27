#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct University{
    int code;
    string name;
    vector<int> studentCodes;
};

void printUniversity(University &u1){
    u1.name = "Universidad DEF";
    cout << u1.code << endl;
    cout << u1.name << endl;
    cout << u1.studentCodes[0] << endl;
}


int main(){
    University u1;
    vector<int> codes;
    codes.push_back(10);
    codes.push_back(20);
    u1.code = 250;
    u1.name = "Universidad ABC";
    u1.studentCodes = codes;

    University u2 = {100, "Universidad XYZ", codes};

    printUniversity(u1);
    cout << u1.name << endl;
    return 0;
}