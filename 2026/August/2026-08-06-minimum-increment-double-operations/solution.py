class Solution:
    def minOperation(self, arr):
        # Stores total number of +1 operations needed
        increments = 0

        # Stores the maximum number of doubling operations
        max_doubles = 0

        # Process each number independently
        for num in arr:

            # Doubling operations required for the current number
            doubles = 0

            # Work backwards until the number becomes zero
            while num > 0:

                # If the number is odd, the last forward operation
                # must have been an increment (+1)
                if num % 2 == 1:
                    increments += 1
                    num -= 1

                # If the number is even, the last forward operation
                # could have been a doubling (*2)
                else:
                    doubles += 1
                    num //= 2

            # Keep only the largest doubling count because
            # doubling affects the entire array simultaneously.
            max_doubles = max(max_doubles, doubles)

        # Minimum operations = all increments + shared doubles
        return increments + max_doubles
