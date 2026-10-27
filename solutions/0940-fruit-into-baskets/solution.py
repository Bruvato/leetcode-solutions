class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)

        hm = {}
        f = 0

        l = 0
        res = 1

        for r in range(n):
            fruit = fruits[r]

            if fruit not in hm:
                f += 1
            
            hm[fruit] = hm.get(fruit, 0) + 1

            while f > 2:
                hm[fruits[l]] -= 1

                if hm[fruits[l]] == 0:
                    del hm[fruits[l]]
                    f -= 1

                l += 1
            
            res = max(res, r - l + 1)

        return res
