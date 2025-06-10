import java.util.*;

public class Main {

    static String getNumasMbase(int o) {
        if (o < 10) {
            return String.valueOf(o);
        } else {
            return String.valueOf((char)(o - 10 + 'A'));
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        in.close();

        String ans = "";
        if (n == 0) {
            ans = "0";
        } else {
            while (n > 0) {
                int o = n % m;
                n = n / m;
                ans = getNumasMbase(o) + ans;
            }
        }

        System.out.println(ans);
    }
}
