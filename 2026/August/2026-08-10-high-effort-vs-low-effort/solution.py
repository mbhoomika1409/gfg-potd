class Solution:
    def maxTask(self, h, l):
        n = len(h)

        # Maximum tasks up to the previous day
        prev1 = max(h[0], l[0])

        # Maximum tasks up to the day before the previous day
        prev2 = 0

        for i in range(1, n):
            # Option 1: Do low-effort task today
            low = prev1 + l[i]

            # Option 2: Do high-effort task today
            # So, no task should be done yesterday
            high = prev2 + h[i]

            # Option 3: Do no task today
            nothing = prev1

            current = max(low, high, nothing)

            prev2 = prev1
            prev1 = current

        return prev1
