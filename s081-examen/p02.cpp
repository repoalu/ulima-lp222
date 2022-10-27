#include <iostream>
#include <string>
using namespace std;

void printText(string &text){
    text[0] = 'X';
    for(int i = 0; i < text.size(); i++){
        char s = text[i];
        cout << s << endl;
    }
    cout << text << endl;
}


int main(){
    string text = "abcde";
    printText(text);
    cout << text << endl;
}