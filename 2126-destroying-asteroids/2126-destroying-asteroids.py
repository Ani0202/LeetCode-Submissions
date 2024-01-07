class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for w in asteroids:
            if w > mass:
                return False
            mass += w

        return True
        