# Time Complexity: O(log n) for get, O(1) for set
# Space Complexity: O(m) where m is the number of entries in the TimeMap

class TimeMap:

    def __init__(self):
        self.timeline = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize the list for the key if it doesn't exist
        if key not in self.timeline:
            self.timeline[key] = []
        # Append the (value, timestamp) pair to the list for the key
        self.timeline[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Retrieve the list of (value, timestamp) pairs for the key
        values = self.timeline.get(key, [])
        
        # Binary search to find the largest timestamp less than or equal to the given timestamp
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            
            # If the mid timestamp is less than or equal to the given timestamp, move right
            if values[mid][1] <= timestamp:
                left = mid + 1
                res = values[mid][0]
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)