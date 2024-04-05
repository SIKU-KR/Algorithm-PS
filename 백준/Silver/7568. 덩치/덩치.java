import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Person> list = new ArrayList<>();
        // 입력
        int n = sc.nextInt();
        for (int i = 0; i<n; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            list.add(new Person(a,b,i));
        }
        for(Person a: list){
            for(Person b: list){
                if((a.weight < b.weight) && (a.height < b.height)){
                    a.biggerCount ++;
                }
            }
            a.rank = a.biggerCount + 1;
        }
        list.sort((o1, o2)->(o1.index-o2.index));
        for(Person a: list){
            System.out.print(a.rank + " ");
        }
    }
}

class Person{
    int weight;
    int height;
    int rank = 0;
    int biggerCount = 0;
    int index;

    Person(int a, int b, int c){
        this.weight = a;
        this.height = b;
        this.index = c;
    }
}