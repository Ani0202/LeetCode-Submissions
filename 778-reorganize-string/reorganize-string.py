class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for i in s:
            count[i] += 1

        prev_char, prev_freq = "", 0
        heap = []
        for k, v in count.items():
            heap.append((-v, k))

        heapq.heapify(heap)
        ans = ""
        while heap or prev_freq:
            if not heap and prev_freq:
                return ""

            freq, char = heapq.heappop(heap)
            ans += char
            freq += 1
            if prev_freq:
                heapq.heappush(heap, (prev_freq, prev_char))
                prev_char, prev_freq = "", 0

            prev_char = char
            prev_freq = freq

        return ans
