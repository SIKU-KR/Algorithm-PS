import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] isvisited;
    static int[][] cabbage;
    static int m, n, k;
    static int count;
    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };

    public static void dfs(int x, int y) {
        isvisited[x][y] = true;
        for(int i = 0; i < 4; i++){
            int cx = dx[i] + x;
            int cy = dy[i] + y;

            if(cx >= 0 && cy >= 00 && cx < m && cy < n){
                if(!isvisited[cx][cy] && cabbage[cx][cy] == 1){
                    dfs(cx, cy);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for (int t = 0; t < tc; t++) {
            count = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            cabbage = new int[m][n];
            isvisited = new boolean[m][n];
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                cabbage[x][y] = 1;
            }
            // dfs 연산부분
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    // 양배추가 있는데 방문하지 않은경우.
                    if (cabbage[i][j] == 1 && !isvisited[i][j]) {
                        count++;
                        dfs(i, j);
                    }
                }
            }
            System.out.println(count);
        }
    }
}