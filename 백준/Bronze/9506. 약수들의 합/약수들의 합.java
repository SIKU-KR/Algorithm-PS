import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while (true) {
            int n = input.nextInt();
            if (n == -1) break;
            System.out.println(calculate(n));
        }
        input.close();
    }

    private static String calculate(int n) {
        if (n <= 1) {
            return n + " is NOT perfect.";
        }

        int total = 0;
        List<Integer> divisors = new ArrayList<>();

        for (int i = 1; i <= n / 2; i++) {
            if (n % i == 0) {
                divisors.add(i);
                total += i;
            }
        }

        if (total == n) {
            StringBuilder sb = new StringBuilder();
            sb.append(n).append(" = ");
            for (int i = 0; i < divisors.size(); i++) {
                if (i > 0) sb.append(" + ");
                sb.append(divisors.get(i));
            }
            return sb.toString();
        } else {
            return n + " is NOT perfect.";
        }
    }
}
