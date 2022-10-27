#include <iostream>
#include "util/tmp/linkedlist_full.hpp"
using namespace std;

int sumValues(Node* head){
    Node* ptr = head;
    int total = 0;
    while(ptr != nullptr){
        cout << ptr->value << endl;
        total += ptr->value;
        ptr = ptr->next;
    }
    return total;
}


int main(){
    Node* head = nullptr;
    addLast(head, 10);
    addLast(head, 20);
    addLast(head, 30);
    addFirst(head, 5);
    printList(head);
    cout << sumValues(head);

}