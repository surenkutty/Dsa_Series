'''
A vendor sells N dierent colored balloons. Find the rst color that
appears an odd number of times. If all colors appear even times, print
"All are even"
'''

def balloon_color(colors):
    color_count = {}
    
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
            
    for color, count in color_count.items():
        if count % 2 != 0:
            return color
            
    return "All are even"