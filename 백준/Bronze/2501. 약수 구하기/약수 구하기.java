import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int k = input.nextInt();
        input.close();
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                cnt++;
                if (cnt == k) {
                    System.out.println(i);
                    return;
                }
            }
        }
        System.out.println(0);
    }
}
