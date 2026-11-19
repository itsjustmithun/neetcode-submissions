class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n 

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for neigh in adj[node]:
                if not visit[neigh]:
                    visit[neigh] = True
                    dfs(neigh)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res
        