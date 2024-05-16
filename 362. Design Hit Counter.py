from collections import deque
class HitCounter:

    def __init__(self):
        self.q = deque()

    """
    @param timestamp: the timestamp
    @return: nothing
    """
    def hit(self, timestamp: int):
        self.q.append(timestamp)

    """
    @param timestamp: the timestamp
    @return: the count of hits in recent 300 seconds
    """
    def get_hits(self, timestamp: int) -> int:
        while len(self.q) > 0 and timestamp - 300 >= self.q[0]:
            self.q.popleft()
        return len(self.q)
