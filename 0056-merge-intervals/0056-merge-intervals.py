class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals by starting value
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # Step 2: Traverse remaining intervals
        for start, end in intervals[1:]:

            last_end = merged[-1][1]

            # Overlapping interval
            if start <= last_end:
                merged[-1][1] = max(last_end, end)

            # Non-overlapping interval
            else:
                merged.append([start, end])

        return merged