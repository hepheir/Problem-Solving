import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.StringBuilder;

public class Main {
    final static int MAX_N = 1000000;
    final static boolean isPrime[] = new boolean[MAX_N+1];
    public static void main(String[] args) throws Exception {
        eratos();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        StringBuilder sb = new StringBuilder();
        
        int m = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);
        br.close();

        for (int i=m; i<=n; i++) {
            if (isPrime[i]) {
                sb.append(i).append('\n');
            }
        }
        System.out.println(sb);
    }

    private static void eratos() {
        int i, j;
        for (i=0; i<2; i++) {
            isPrime[i] = false;
        }
        for (i=2; i<MAX_N; i++) {
            isPrime[i] = true;
        }
        for (i=2; i<=Math.sqrt(MAX_N)+1; i++) {
            for (j=2*i; j<=MAX_N; j+=i) {
                isPrime[j] = false;
            }
        }
    }
}