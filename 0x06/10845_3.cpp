#include <bits/stdc++.h>
using namespace std;
int q[10000];
int head = 0, tail = 0;

void push(int x) {
    q[tail++] = x;
}

void pop() {
    head++;
}

int size() {
    return tail - head;
}

int empty() {
    return head == tail;
}

int front() {
    return q[head];
}

int back() {
    return q[tail - 1];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    while (n--) {
        string cmd;
        cin >> cmd;
        if (cmd == "push") {
            int x;
            cin >> x;
            push(x);
        }
        else if (cmd == "pop") {
            if (empty()) cout << "-1\n";
            else {
                cout << front() << '\n';
                pop();
            }
        }
        else if (cmd == "size") {
            cout << size() << '\n';
        }
        else if (cmd == "empty") {
            cout << empty() << '\n';
        }
        else if (cmd == "front") {
            if (empty()) cout << "-1\n";
            else cout << front() << '\n';
        }
        else { // "back"
            if (empty()) cout << "-1\n";
            else cout << back() << '\n';
        }
    }
}