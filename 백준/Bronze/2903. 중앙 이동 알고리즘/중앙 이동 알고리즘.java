import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.close();
        System.out.println(calculate(n));
    }

    private static String calculate(int n) {
        int value = 1;
        for (int i = 0; i < n; i++) {
            value *= 2;
        }
        int points = value + 1;
        return String.valueOf(points * points);
    }
}
