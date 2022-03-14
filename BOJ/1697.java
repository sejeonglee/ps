import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class State {
    int position;
    int minutes;

    public State(int position, int minutes) {
        this.position = position;
        this.minutes = minutes;
    }
}

class SearchQueue {
    private Queue<State> queue;
    private boolean[] visited;
    private Integer answer;
    private int destination;

    public SearchQueue(int position, int destination, int size) {
        this.visited = new boolean[size + 5];
        this.queue = new LinkedList<>();
        this.destination = destination;
        this.answer = null;

        if (position == destination) {
            this.answer = 0;
        }

        enqueue(new State(position, 0));
    }

    public boolean isEmpty() {
        return this.queue.isEmpty();
    }

    public Integer seekAnswer() {
        return this.answer;
    }

    public void Next() {
        if (this.answer != null) {
            return;
        }

        State current = this.queue.poll();
        addNextSteps(current);
    }

    private void addNextSteps(State state) {
        ArrayList<Integer> nextValues = new ArrayList<>(Arrays.asList(
                state.position * 2,
                state.position + 1,
                state.position - 1));
        for (Integer nextValue : nextValues) {
            if (this.destination == nextValue) {
                this.answer = state.minutes + 1;
                break;
            }
            this.enqueue(new State(nextValue, state.minutes + 1));
        }
    }

    private void enqueue(State state) {
        if (state.position < 0 || state.position >= this.visited.length
                || this.visited[state.position]) {
            return;
        }
        this.queue.add(state);
        this.visited[state.position] = true;
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        final int MAX_SIZE = 100000;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        sc.close();

        SearchQueue sq = new SearchQueue(N, K, MAX_SIZE);

        while (!sq.isEmpty() && sq.seekAnswer() == null) {
            sq.Next();
        }

        System.out.println(sq.seekAnswer());
    }
}
package BOJ;

public class 1697 {
  
}
