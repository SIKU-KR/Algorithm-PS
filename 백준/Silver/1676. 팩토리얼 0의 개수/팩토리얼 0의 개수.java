import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static int n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        BigInteger fact = BigInteger.valueOf(1);
        while (n > 0) {
            fact = fact.multiply(BigInteger.valueOf(n));
            n--;
        }
        char[] result = fact.toString().toCharArray();
        int index = result.length-1;
        int count = 0;
        while(true){
            if(result[index] == '0'){
                count++;
            } else {
                break;
            }
            index--;
        }
        System.out.println(count);
    }
}