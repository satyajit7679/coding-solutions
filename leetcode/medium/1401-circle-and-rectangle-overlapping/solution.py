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