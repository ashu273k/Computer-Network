import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class Dijkstra {

   public class Pair {
        int node, weight;

        Pair(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }
    
   }

   public int[] solve(int A, int[][] B, int C) {

        List<List<Pair>> graph = new ArrayList<>();

        for (int i = 0; i < A; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge: B) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph.get(u).add(new Pair(v, w));
            graph.get(v).add(new Pair(u, w));
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>(Comparator.comparingInt(p -> p.weight));

        // distance array
        int[] D = new int[A];
        Arrays.fill(D, Integer.MAX_VALUE);
        D[C] = 0;

        pq.add(new Pair(C, 0));
        while (!pq.isEmpty()) {
            Pair curr = pq.poll();

            int u = curr.node;
            int d = curr.weight;

            if (d > D[u]) continue;         // Already shorter path available skip the route

            for (Pair edge: graph.get(u)) {
                int v = edge.node;
                int w = edge.weight;    
                
                if (D[v] > D[u] + w) { // checking if the distance set is minimum or not if not then setting weight + previous nod
                    D[v] = D[u] + w;
                    pq.add(new Pair(v, D[v]));  // Even if v is already in PQ with an older distance, we keep both; the older one will be ignored later by the if (d > D[u]) continue check.
                }
            }

        }
        
        for (int i = 0; i < A; i++) {
            if (D[i] == Integer.MAX_VALUE) D[i] = -1;
        }

        return D;
   }


}
