class Allocator {
public:
    vector<int> mem;

    Allocator(int n) : mem(n, 0) {}

    int allocate(int size, int mID) {
        int n = mem.size();
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (mem[i] != 0) {
                count = 0; // reset on occupied cell
            } else {
                count++;
                if (count == size) {
                    // Found a valid block — fill it
                    int start = i - size + 1;
                    fill(mem.begin() + start, mem.begin() + start + size, mID);
                    return start;
                }
            }
        }
        return -1;
    }

    int freeMemory(int mID) {
        int freed = 0;
        for (int& cell : mem) {
            if (cell == mID) {
                cell = 0;
                freed++;
            }
        }
        return freed;
    }
};

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->freeMemory(mID);
 */
