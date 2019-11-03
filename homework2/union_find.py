class Subset(object):
    def __init__(self, parent):
        self.parent = parent
        self.rank = 0
    def __repr__(self):
        return str(self.parent)

def find(subsets, i):
    """
    finds root and makes root parent of i
    (path compression)
    subsets = list of Subset objects
    """
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)
    return subsets[i].parent

def union(subsets, x, y):
    """
    union by rank (put lower rank element under tree)
    """
    x_root = find(subsets, x)
    y_root = find(subsets, y)

    if (subsets[x_root].rank < subsets[y_root].rank):
        subsets[x_root].parent = y_root
    elif (subsets[x_root].rank > subsets[y_root].rank):
        subsets[y_root].parent = x_root
    else:
        subsets[y_root].parent = x_root
        subsets[x_root].rank += 1
