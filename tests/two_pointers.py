from typing import *

### Two Pointers

## Not working right now

# Expected: O(a), Actual: O()
def maxArea(height: List) -> int:
    l = 0
    r = len(height) - 1
    result = 0

    while l <= r:
        area = min(height[l], height[r]) * (r - l)

        result = max(result, area)

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return result