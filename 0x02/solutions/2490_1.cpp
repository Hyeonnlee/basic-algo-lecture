#include <bits/stdc++.h>
using namespace std;
int a[4];

int main(){
    for (int i = 0; i < 3; i++){
        int back = 0;
        for (int j = 0; j < 4; j++){
            cin >> a[j];
            if (a[j] == 0) back++;
        }
        if (back == 1) cout << "A\n";
        else if (back == 2) cout << "B\n";
        else if (back == 3) cout << "C\n";
        else if (back == 4) cout << "D\n";
        else cout << "E\n";
    }
}