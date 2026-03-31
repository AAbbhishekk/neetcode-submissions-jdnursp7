class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src,dest in edges:
            adj[src].append(dest)

        topsort = []
        visited = set()
        visiting = set()

        def dfs(src):

            if src in visited:
                return True
            if src in visiting:
                return False
            
            visiting.add(src)

            for neighbour in adj[src]:
                if not dfs(neighbour):
                    return False
            visiting.remove(src)
            visited.add(src)
            topsort.append(src)

            return True

        for i in range(n):
            if not dfs(i):
                return []
        topsort.reverse()
        return topsort



        