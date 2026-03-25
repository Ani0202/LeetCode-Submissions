class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 1000000007
        inventory.sort(reverse=True)
        inventory.append(0)

        max_profit = 0
        balls_count = 1

        for i in range(len(inventory) - 1):
            diff = inventory[i] - inventory[i + 1]

            if diff == 0:
                balls_count += 1
                continue

            balls = diff * balls_count

            if balls <= orders:
                sum_per_col = (inventory[i] + inventory[i + 1] + 1) * diff // 2
                max_profit = (max_profit + sum_per_col * balls_count) % mod

                orders -= balls
            else:
                full_rows = orders // balls_count
                rem = orders % balls_count

                if full_rows > 0:
                    sum_per_col = (
                        (inventory[i] + (inventory[i] - full_rows + 1)) * full_rows // 2
                    )
                    max_profit = (max_profit + sum_per_col * balls_count) % mod

                next_row_value = inventory[i] - full_rows
                max_profit = (max_profit + rem * next_row_value) % mod

                break

            balls_count += 1

        return max_profit
