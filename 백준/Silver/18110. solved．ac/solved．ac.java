import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // input
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i<n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        // cal
        int exception = (int) (n * 0.15 + 0.5);
        Arrays.sort(arr);
        double sum = 0;
        for (int i = exception; i < n - exception; i++) {
            sum = sum + arr[i];
        }
        double count = n - (exception * 2);
        int result = (int) ((sum / count) + 0.5);
        // output
        System.out.println(result);
    }
}