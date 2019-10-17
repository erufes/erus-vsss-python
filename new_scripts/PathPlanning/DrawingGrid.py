from .Graph import GridGraph
def draw_tile(graph, c, style, width):
    r = "."
    if 'number' in style and c in style['number']: r = "%d" % style['number'][c]
    if 'point_to' in style and style['point_to'].get(c, None) is not None:
        (x1, y1) = c
        (x2, y2) = style['point_to'][c]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and c == style['start']: r = "A"
    if 'goal' in style and c == style['goal']: r = "Z"
    if 'path' in style and c in style['path']: r = "@"
    if c in list(map(lambda x : graph.transform2Cart(x), graph.whatIsOccupied())) : r = "#" * width
    return r

def draw_grid(graph, width=2, **style):
    nx, ny = graph.grid
    for y in range(ny):
        for x in range(nx):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()
