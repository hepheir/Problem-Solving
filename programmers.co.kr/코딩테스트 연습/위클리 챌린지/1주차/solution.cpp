long long solution(int price, int money, int count)
{
    int i, j;
    long long answer = money;
    for (i = 0; i < count; i++)
    {
        for (j = 0; j <= i; j++)
        {
            answer -= price;
        }
    }
    return (answer < 0) ? -answer : 0;
}