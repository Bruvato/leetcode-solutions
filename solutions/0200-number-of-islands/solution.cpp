class Solution {
public:
    vector<vector<char>> grid;
    set<pair<int, int>> seen;
    int m;
    int n;
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        m = grid.size();
        n = grid[0].size();
        this->grid = grid;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1' and !seen.contains({r,c})) {
                    bfs(r, c);
                    res++;
                }
            }
        }

        return res;
    }

    void bfs(int r, int c) {
        seen.insert({r, c});
        queue<pair<int, int>> q;

        q.push({r, c});

        while (!q.empty()) {
            auto [row, col] = q.front();
            q.pop();

            for (auto [x, y] : dirs) {
                int nr = row + y;
                int nc = col + x;

                if (nr < 0 || nr >= m || nc < 0 || nc >= n)
                    continue;
                if (grid[nr][nc] != '1')
                    continue;
                if (seen.contains({nr, nc}))
                    continue;

                seen.insert({nr, nc});
                q.push({nr,nc});
            }
        }
    }
};
