class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = collections.deque(range(len(tickets)))
        seconds = 0
        while q:
            i = q.popleft()
            tickets[i] -= 1
            seconds += 1
            if i == k and tickets[i] == 0:
                return seconds
            if tickets[i] > 0:
                q.append(i)
        return seconds