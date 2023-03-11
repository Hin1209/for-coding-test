import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

t = int(input())

def main(t):
    for _ in range(t):
        n, m, k = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        dp = [[INF] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = [INF, 0]
        dp[1][0][0] = 0
        dp[1][0][1] = 0
        for _ in range(k):
            start, end, cost, time = map(int, input().split())
            graph[start].append((end, cost, time))
            
        h = [] 
        min_travel = INF
        heapq.heappush(h, (0, 0, 1))
        while h:
            time, cost, now = heapq.heappop(h)
            if now == n: 
                min_travel = min(min_travel, time)
                break
            for next_node, c, t in graph[now]:
                next_cost = cost + c
                next_time = time + t
                if next_cost > m: continue
                if dp[next_node][next_cost] > next_time:
                    if dp[next_node][0][0] < next_cost and dp[next_node][0][1] < next_time:
                        continue
                    elif dp[next_node][0][0] > next_cost:
                        dp[next_node][0][0] = next_cost
                        dp[next_node][0][1] = next_time
                    elif dp[next_node][0][1] > next_time:
                        dp[next_node][0][0] = next_cost
                        dp[next_node][0][1] = next_time
                    dp[next_node][next_cost] = next_time
                    heapq.heappush(h, (next_time, next_cost, next_node))
        print(min_travel) if min_travel < INF else print("Poor KCM")
main(t) 