class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        
        rem = 1 % k
        count = 1

        seen = set()

        while rem != 0:
            rem = (10 * rem + 1) % k
            count += 1

            if rem in seen or count > k:
                return -1
            
            seen.add(rem)
        
        return count
