#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int a = 12, b = 6;
    int ans = 0;
    int n = min(a, b);
    for(int i = 1; i <= n; i++)
    {
        if(a % i == 0 && b % i == 0)
        {
            cout << i << endl;
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}