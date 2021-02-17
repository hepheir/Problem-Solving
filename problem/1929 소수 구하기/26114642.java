import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final int MAX_N = 1000000;
        boolean arr[] = new boolean[MAX_N+1];
        eratos(arr, MAX_N);

        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        scanner.close();

        for (int i=m; i<=n; i++) {
            if (arr[i])
                System.out.println(i);
        }
    }

    public static void eratos(boolean[] array, final int size) {
        for (int i=2; i<size; i++)
            array[i] = true;

        array[0] = false;
        array[1] = false;
        for (int i=2; i<=Math.sqrt(size)+1; i++) {
            for (int j=2*i; j<=size; j+=i) {
                array[j] = false;
            }
        }
    }
}