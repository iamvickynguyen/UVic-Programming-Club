/*
	Jack Basha
	Student of University of Victoria
*/

#include<bits/stdc++.h>
#define loop(i, n) 		for(i = 0 ; i < n ; i++)
#define loop_x(i, x, n) for(i = x ; i < n ; i++)
#define FAST ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0)
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pair<int,int> > vpi;
typedef pair<int,int> ii;

class Item
{
public:
    int value, weight;
};

const int MAX_N = 2001, MAX_C = 2001;
int dp[MAX_N][MAX_C]/*, predecessor[MAX_N]*/;
int n, capacity;
vector<int> ansVector;
Item arr[MAX_N];

int knapsack(int i, int curr_weight)
{
    if(i == n)
        return 0;

    if(dp[i][curr_weight] != -1)
    {
        return dp[i][curr_weight];
    }

    if(curr_weight + arr[i].weight > capacity)  // can't take i
        dp[i][curr_weight] = knapsack(i + 1, curr_weight);
    else
        dp[i][curr_weight] = max(
            knapsack(i + 1, curr_weight),
            arr[i].value + knapsack(i + 1, curr_weight + arr[i].weight));

    return dp[i][curr_weight];
//    dp[i][curr_weight] = knapsack(i + 1, last_taken_idx, curr_weight, curr_value);
//    int returner = knapsack(i + 1, i, curr_weight + arr[i].weight, curr_value + arr[i].value);
//
//    if(returner > dp[i][curr_weight])
//    {
//        predecessor[i] = last_taken_idx;
//        dp[i][curr_weight] = returner;
//    }
//
//    return dp[i][curr_weight];
}

void print_solution(int i, int curr_weight)
{
    // trace function
    if(curr_weight > capacity || i == n)
        return;

    if(dp[i][curr_weight] == knapsack(i + 1, curr_weight))   // we didn't take i
    {
        print_solution(i + 1, curr_weight);
    }
    else    // we took i
    {
        ansVector.push_back(i);
        print_solution(i + 1, curr_weight + arr[i].weight);
    }
}

int main()
{
	FAST;
    int i, j, v, w;

	while(scanf("%d %d", &capacity, &n) == 2)
    {
        ansVector.clear();
        loop(i, n)
        {
//            predecessor[i] = -1;
            loop(j, MAX_C)
            {
                dp[i][j] = -1;
            }
        }

        loop(i, n)
        {
            scanf("%d %d", &v, &w);
            arr[i].value = v;
            arr[i].weight = w;
        }

        int ans = knapsack(0, 0);
        /*
        w = 0;
        v = 0;

        loop_x(i, 1, n)
        {
            if(dp[i][w] != ans)
            {
                if(dp[i][w + arr[i - 1].weight] == ans)
                {
                    w += arr[i - 1].weight;
                    v += arr[i - 1].value;
                    ansVector.push_back(i - 1);
                }
            }
        }

        if(v != ans)
            ansVector.push_back(n - 1);
        */

        print_solution(0, 0);

        /*
        loop(i, n)
        {
            loop(j, capacity)
            {
                printf("%d ", dp[i][j]);
            }
            printf("\n");
        }
        */

        printf("%d\n", ansVector.size());
        loop(i, ansVector.size())
        {
            printf("%d", ansVector[i]);
            if(i != ansVector.size() - 1)
                printf(" ");
        }

        printf("\n");
    }

    return 0;
}
