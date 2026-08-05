class Solution:
    def countSubarrays(self, arr, l, r):

        # Function to count subarrays whose sum is <= k
        def count(k):

            left = 0          # Left pointer of the sliding window
            curr_sum = 0      # Stores the current window sum
            ans = 0           # Stores total valid subarrays

            # Expand the window by moving the right pointer
            for right in range(len(arr)):

                # Include the current element in the window
                curr_sum += arr[right]

                # If the sum becomes greater than k,
                # shrink the window from the left
                while curr_sum > k:
                    curr_sum -= arr[left]
                    left += 1

                # All subarrays ending at 'right'
                # and starting from 'left' to 'right'
                # have sum <= k
                ans += right - left + 1

            return ans

        # Required answer:
        # (subarrays with sum <= r)
        # -
        # (subarrays with sum <= l - 1)
        return count(r) - count(l - 1)
