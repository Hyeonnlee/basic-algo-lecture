#include <bits/stdc++.h>
using namespace std;
const int MX = 10000;
int arr[2 * MX + 1];
int head = MX, tail = MX;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    while (n--) {
        string cmd;
        cin >> cmd;
        if (cmd == "push_front") cin >> arr[--head];
        else if (cmd == "push_back") cin >> arr[tail++];
        else if (cmd == "pop_front") cout << (head == tail ? -1 : arr[head++]) << '\n';
        else if (cmd == "pop_back") cout << (head == tail ? -1 : arr[--tail]) << '\n';
        else if (cmd == "size") cout << tail - head << '\n';
        else if (cmd == "empty") cout << (head == tail ? 1 : 0) << '\n';
        else if (cmd == "front") cout << (head == tail ? -1 : arr[head]) << '\n';
        else cout << (head == tail ? -1 : arr[tail - 1]) << '\n';
    }
}