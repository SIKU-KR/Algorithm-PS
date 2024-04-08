import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

import static java.lang.Math.pow;

public class Main {
    static int m = 1234567891;
    static int r = 31;

    static int getHashValue(int i, char c) {
        return (int)((((int) c)-96) * pow(r, i));
    }

    public static void main(String[] args) {
        int integer = 0;
        Scanner sc = new Scanner(System.in);
        int l = sc.nextInt();
        sc.nextLine();
        String str = sc.nextLine();

        for(int i = 0; i < l; i++){
            integer = integer + getHashValue(i, str.charAt(i));
            integer = integer % m;
        }

        // int result = integer / r;
        System.out.println(integer);
    }
}