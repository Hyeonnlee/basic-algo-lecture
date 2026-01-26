#include <bits/stdc++.h>
using namespace std;
int alphabet[26];
string str;
int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> str;
    for (char s: str) alphabet[s - 'a'] += 1;
    for (int i = 0; i < 26; i++) cout << alphabet[i] << " ";
}