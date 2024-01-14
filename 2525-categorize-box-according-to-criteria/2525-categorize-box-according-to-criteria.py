class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = False
        isHeavy = False
        if length >= 10000 or width >= 10000 or height >= 10000 or (length * width * height) >= 1000000000:
            isBulky = True
        if mass >= 100:
            isHeavy = True
        if isBulky and isHeavy:
            return "Both"
        elif isBulky:
            return "Bulky"
        elif isHeavy:
            return "Heavy"
        return "Neither"
        