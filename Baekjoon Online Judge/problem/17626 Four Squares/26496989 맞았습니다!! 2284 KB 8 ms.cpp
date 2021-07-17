#include <iostream>
#include <cstring> // memset() 함수 사용 위함.

#define MAX_N 50000

int main(void)
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int squares[MAX_N+1];
    int dp[MAX_N+1]; // 동적 프로그래밍을 위한 저장공간
    int n;

    dp[0] = 0;
    for (int i=1; i<=MAX_N; i++)
    {
        // N개의 제곱수는 미리 구해놓고 사용
        squares[i] = i*i;

        // 문제에서 50000 이하의 수는 최대 4개 이하의 자연수로 만들 수 있음이 보장됨.
        dp[i] = 4;
    }

    std::cin >> n;

    for (int i=1; i<=n; i++)
    {
        for (int j=1; squares[j]<=i && dp[i]; j++)
            dp[i] = std::min(dp[i-squares[j]], dp[i]);

        dp[i] += 1; // 0 base -> 1 base
    }

    std::cout << dp[n] << std::endl;
    return 0;
}