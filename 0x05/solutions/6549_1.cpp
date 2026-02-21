// stack<pair<height, index>>를 사용한 풀이
#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    while (1) {
        int n;
        cin >> n;
        if (n == 0) break;

        stack<pair<long long, int>> s;
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            long long h;
            cin >> h;

            int start = i;
            while (!s.empty() && s.top().first > h) {
                long long height = s.top().first;
                int idx = s.top().second;
                s.pop();

                long long width = i - idx;
                ans = max(ans, height * width);
                start = idx;
            }
            s.push({h, start});
        }

        while (!s.empty()) {
            long long height = s.top().first;
            long long width = n - s.top().second;
            ans = max(ans, height * width);
            s.pop();
        }

        cout << ans << '\n';
    }
}