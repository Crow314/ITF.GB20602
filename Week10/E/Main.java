import java.io.IOException;
import java.io.InputStream;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        FastScanner sc = new FastScanner();

        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();

        List<List<Tram>> trams = new ArrayList<>(n);
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

        PriorityQueue<Node> queue = new PriorityQueue<>();

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

class Node implements Comparable<Node> {
    int u;
    int cost;

    Node(int u, int cost) {
        this.u = u;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        }else{
            ptr = 0;
            try {
                buflen = in.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (buflen <= 0) {
                return false;
            }
        }
        return true;
    }
    private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
    private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
    public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while(isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0' <= b && b <= '9') {
                n *= 10;
                n += b - '0';
            }else if(b == -1 || !isPrintableChar(b)){
                return minus ? -n : n;
            }else{
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }
    public int nextInt() {
        long nl = nextLong();
        if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
        return (int) nl;
    }
    public double nextDouble() { return Double.parseDouble(next());}
}
