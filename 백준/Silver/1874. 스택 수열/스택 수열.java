import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> stk = new Stack<>();
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < n; i++){
            q.add(sc.nextInt());
        }

        StringBuilder result = new StringBuilder();
        for(int i = 1; i <= n; i++){
            if (stk.empty()){
                stk.push(i);
                result.append("+\n");
            } else if(!stk.peek().equals(q.peek())){
                stk.push(i);
                result.append("+\n");
            } else if(stk.peek().equals(q.peek())){
                while (!stk.empty() && stk.peek().equals(q.peek())){
                    stk.pop();
                    result.append("-\n");
                    q.remove();
                }
                stk.push(i);
                result.append("+\n");
            }
        }
        while (!stk.empty() && stk.peek().equals(q.peek())){
            stk.pop();
            result.append("-\n");
            q.remove();
        }
        if(stk.empty() && q.isEmpty()){
            System.out.print(result.toString());
        }else {
            System.out.println("NO");
        }
    }
}