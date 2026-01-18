#include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    for (int i = 0; i < N - 1; i++){
        for (int j = 0; j < i; j++) cout << ' ';
        for (int j = 0; j < 2 * (N - i) - 1; j++) cout << '*';
        cout << "\n";
    }

    for (int i = 0; i < N - 1; i++) cout << ' ';
    cout << "*\n";
    // ''은 char, ""은 string
    // ''에 문자 여러 넣으면 에러

    for (int i = 1; i <= N - 1; i++){
        for (int j = 0; j < N - i - 1; j++) cout << ' ';
        for (int j = 0; j < 2 * i + 1; j++) cout << '*';
        cout << "\n";
    }
}