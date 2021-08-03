long long solution(int price, int money, int count)
{
    int i, j;
    long long answer = money;
    for (i=0;i<count;i++) {
        for (j=0;j<=i;j++) {
            answer -= price;
        }
    }
    if (answer < 0) return -answer;
    else return 0;
}