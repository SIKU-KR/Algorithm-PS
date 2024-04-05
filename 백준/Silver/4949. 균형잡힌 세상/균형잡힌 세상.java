import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> list = new ArrayList<>();
        // 입력
        while(true) {
            String tmp = br.readLine();
            if(tmp.equals(".")) {
                break;
            }
            else {
                list.add(tmp);
            }
        }
        // 검사 및 출력
        for(String s : list) {
            boolean check = true;
            Stack<Integer> stk = new Stack<>();
            char[] arr = s.toCharArray();
            for(char c : arr) {
                try {
                    if (c == '(') {
                        stk.push(1);
                    } else if (c == '[') {
                        stk.push(2);
                    } else if (c == ')') {
                        if (!stk.pop().equals(1)) {
                            check = false;
                            break;
                        }
                    } else if (c == ']') {
                        if (!stk.pop().equals(2)) {
                            check = false;
                            break;
                        }
                    }
                } catch(EmptyStackException e) {
                    check = false;
                    break;
                }
            }
            if(!check || !stk.empty())
                System.out.println("no");
            else
                System.out.println("yes");
        }
    }
}