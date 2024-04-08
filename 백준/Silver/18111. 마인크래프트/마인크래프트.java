import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int max = -1;
        int min = 999;
        int[][] arr = new int[n][m];

        // 배열 입력 및 최대 최소 찾기
        for(int i = 0; i < n; i++){
            StringTokenizer rowTokens = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++) {
                int input = Integer.parseInt(rowTokens.nextToken());
                arr[i][j] = input;
                if(input > max) max = input;
                if(input < min) min = input;
            }
        }
        // 브루트포스 알고리즘
        int bestTime = 2100000000;
        int bestI = -1;
        for(int i = min; i <= max; i++){
            int time = 0;
            int block = b;
            // i 가 기준 블록의 개수
            for (int[] x : arr){
                for(int y : x){
                    if(y < i){
                        // 현재 좌표가 기준블록보다 작은경우 : 블록을 더 놔줘야하는경우
                        int count = i - y;
                        time = time + count;
                        block -= count;
                    } else {
                        // 현재 좌표가 기준블록보다 큰경우 : 블록을 빼줘야하는경우
                        int count = y - i;
                        time = time + count * 2;
                        block += count;
                    }
                }
            }
            // 브루트포스 검사
            if(block >= 0 && bestTime > time) {
                bestI = i;
                bestTime = time;
            } else if (block >= 0 && bestTime == time) {
                bestI = Math.max(bestI, i);
            }
        }
        System.out.println(bestTime + " " + bestI);
    }
}