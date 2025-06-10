import java.util.*;

public class Main {

    static String calculate(int i){
        int q = 0, d = 0, n = 0, p = 0;
        while (i >= 25){
            q += 1;
            i -= 25;
        }
        while (i >= 10) {
            d += 1;
            i -= 10;
        }
        while (i >= 5) {
            n += 1;
            i -= 5;
        }
        while(i > 0) {
            p += 1;
            i -= 1;
        }
        return q + " " + d + " " + n + " " + p;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(input.nextInt());
        }
        input.close();

        for (Integer i: list) {
            System.out.println(calculate(i));
        }

    }
}
