import java.util.*;

public class Main {

    static int getInt(char a){
        if (a >= '0' && a <= '9'){
            return a - '0';
        } else {
            return a - 'A' + 10;
        }
    }

    public static void main(String[] args) {
        // 입력
        Scanner in = new Scanner(System.in);
        String a = in.nextLine();
        in.close();
        // 변수할당
        String[] splited = a.split(" ");
        String str = splited[0];
        int b = Integer.parseInt(splited[1]);

        int result = 0;
        for (int i = 0; i < str.length(); i++) {
            result = result * b + getInt(str.charAt(i));
        }
        System.out.println(result);
    }
}
