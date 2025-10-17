import java.util.Arrays;

public class BellmanFord {
    public int[] solve(int A, int[][] B, int C) {
        final int INF = Integer.MAX_VALUE;
        final long NEG_weight = 100000000L;
        int[] dist = new int[A];
        boolean[] negative_cycles = new boolean[A];

        Arrays.fill(dist, INF);
        dist[C] = 0;
        for (int i = 0; i < A-1; i++) {
            for (int[] edge : B) {
                int u = edge[0], v = edge[1], w = edge[2];
                if (dist[u] != INF && dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        for (int i = 0; i < A; i++) {
            for (int[] edge : B) {
                int u = edge[0], v = edge[1], w = edge[2];
                if (dist[u] != INF && dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    negative_cycles[v] = true;
                }
                if (negative_cycles[u]) {
                    negative_cycles[v] = true;
                }
            }
        }

        int[] results = new int[A];
        for (int i = 0; i < A; i++) {
            if (dist[i] == INF) {
                results[i] = -1;
            } else if (negative_cycles[i]) results[i] = (int)NEG_weight;
            else results[i] = dist[i];
        }
        return results;

        
    }
}
