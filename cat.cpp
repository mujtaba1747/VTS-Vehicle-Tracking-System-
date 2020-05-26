// Seek knowledge from the Cradle to the Grave !!
// https://www.linkedin.com/in/syed-mujtaba

#include <bits/stdc++.h>
using namespace std;
#define int             long long
#define ld              long double
#define ll              long long
#define pb              push_back
#define fi              first
#define se              second
#define MAXN            200064
#define mod             1000000009 // 998244353 // 1e9 + 7
#define MAX             8000000000000000064LL
#define MIN            -8000000000000000064LL
#define mt              make_tuple
#define eps             1e-6
#define endl            '\n'
#define test            int T_T; cin>>T_T; while(T_T--)
#define fast_io         ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

void solve()
{
	int t;
	cin >> t;
	while(t--)
	{
		int n;
		cin >> n;
		int a[n + 1];
		int f[1001] = {'\0'};
		for(int i = 1; i <= n; i++)
		{
			cin >> a[i];
			f[a[i]]++;
		}
		set < int > oc;

		bool F = true;

		for(int i = 1; i <= n; i++)
		{
			if(oc.count(a[i]) != 0)
			{
				F = 0;
				// cout << 1 << endl;
				break;
			}


			oc.insert(a[i]);
			int j;
			for(j = i; j <= n; j++)
				if(a[j] != a[i])
					break;

			i = j - 1;

		}
		set < int > z;
		for(int i = 1; i <= 1000; i++)
		{
			if(f[i] != 0)
			{
				if(z.count(f[i]) != 0)
				{
					F = 0;
					// cout << 2 << endl;
					break;
				}
				z.insert(f[i]);
			}
		}
		if(!F)
		{
			cout << "NO\n";
		}
		else cout << "YES\n";



		
	}
}
signed main()
{
    fast_io
    solve();
    return 0;       
}