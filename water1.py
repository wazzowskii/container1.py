def max_area(h):
    max_water = 0
    left = 0
    right = len(h) - 1

    while left < right:
       
        current_water = min(h[left], h[right]) * (right - left)
        max_water = max(max_water, current_water)

       
        if h[left] < h[right]:
            left += 1
        else:
            right -= 1

    return max_water

h = list(map(int, input("Enter heights of vertical lines separated by space: ").split()))

result = max_area(h)
print("Maximum amount of water the container can store:", result)
