// stack<index>를 사용한 풀이
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (true) {
        int n;
        cin >> n;
        if (n == 0) break;
        
        vector<long long> h(n + 1);
        for (int i = 0; i < n; i++) {
            cin >> h[i];
        }
        h[n] = 0;

        stack<int> s;
        long long ans = 0;
        for (int i = 0; i <= n; i++) {
            while (!s.empty() && h[s.top()] > h[i]) {
                long long height = h[s.top()];
                s.pop();
                long long width;
                if (s.empty()) width = i;
                else width = i - s.top() - 1;
                ans = max(ans, height * width);
            }
            s.push(i);
        }
        cout << ans << '\n';
    }
}