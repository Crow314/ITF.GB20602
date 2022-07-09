import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();

        List<List<Tram>> trams = new ArrayList<>();
        for (int i=0; i<n; i++) {
            trams.add(new ArrayList<>());
        }

        for (int i=0; i<m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int t0 = sc.nextInt();
            int p = sc.nextInt();
            int d = sc.nextInt();

            trams.get(u).add(new Tram(u, v, t0, p, d));
        }

        if (dijkstra(trams, n, 0) <= s) {
            int left = 0;
            int right = s;

            while (left < right) {
                int mid = (right-left) / 2 + left + (left+right)%2; // ceil

                if (dijkstra(trams, n, mid) > s) {
                    right = mid - 1;
                } else {
                    left = mid;
                }
            }

            System.out.println(left);
        } else {
            System.out.println("impossible");
        }
    }

    public static int dijkstra(List<List<Tram>> trams, int n, int startTime) {
        int[] times = new int[n];
        for (int i=0; i<n; i++) {
            times[i] = Integer.MAX_VALUE;
        }

        PriorityQueue<Node> queue = new PriorityQueue<>(new NodeComparator());

        times[0] = startTime;
        queue.add(new Node(0, startTime));

        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int u = node.u;
            int arrivalTime = node.cost;

            if (arrivalTime > times[u]) {
                continue;
            }

            if (u == n-1) {
                break;
            }

            for (Tram tram: trams.get(u)) {
                int v = tram.v;
                int t0 = tram.t0;
                int p = tram.p;
                int d = tram.d;

                int departureTime;
                if (arrivalTime < t0) {
                    departureTime = t0;
                } else {
                    departureTime = (arrivalTime - t0 + p - 1) / p * p + t0;
                }

                int eta = departureTime + d;

                if (eta < times[v]) {
                    times[v] = eta;
                    queue.add(new Node(v, eta));
                }
            }
        }

        return times[n-1];
    }
}

class Tram {
    int u;
    int v;
    int t0;
    int p;
    int d;

    Tram (int u, int v, int t0, int p, int d) {
        this.u = u;
        this.v = v;
        this.t0 = t0;
        this.p = p;
        this.d = d;
    }
}

class Node {
    int u;
    int cost;

    Node(int u, int cost) {
        this.cost = cost;
        this.u = u;
    }
}

class NodeComparator implements Comparator<Node> {
    @Override
    public int compare(Node o1, Node o2) {
        return o1.cost - o2.cost;
    }
}

