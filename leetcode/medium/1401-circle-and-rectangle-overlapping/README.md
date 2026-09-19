# Circle and Rectangle Overlapping

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a circle represented as `(radius, xCenter, yCenter)` and an axis-aligned rectangle represented as `(x1, y1, x2, y2)`, where `(x1, y1)` are the coordinates of the bottom-left corner, and `(x2, y2)` are the coordinates of the top-right corner of the rectangle.

Return `true` *if the circle and rectangle are overlapped otherwise return* `false`. In other words, check if there is  **any**  point `(xi, yi)` that belongs to the circle and the rectangle at the same time.

 

 **Example 1:** 

```
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

```

 **Example 2:** 

```
Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

```

 **Example 3:** 

```
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

```

 

 **Constraints:** 

- 1 <= radius <= 2000
- -104 <= xCenter, yCenter <= 104
- -104 <= x1 < x2 <= 104
- -104 <= y1 < y2 <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.4 MB (beats 18.67%)  
**Submitted:** 2026-09-19T17:14:33.335Z  

```py
class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        
        # Find closest x-coordinate in rectangle
        if xCenter < x1:
            closest_x = x1
        elif xCenter > x2:
            closest_x = x2
        else:
            closest_x = xCenter

        # Find closest y-coordinate in rectangle
        if yCenter < y1:
            closest_y = y1
        elif yCenter > y2:
            closest_y = y2
        else:
            closest_y = yCenter

        # Distance squared
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        distance_squared = dx * dx + dy * dy

        return distance_squared <= radius * radius
```

---

[View on LeetCode](https://leetcode.com/problems/circle-and-rectangle-overlapping/)