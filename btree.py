class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

def split_child(self, x, i, y):
    z = BTreeNode(y.leaf)
    x.children.insert(i + 1, z)
    x.keys.insert(i, y.keys[self.t - 1])
    z.keys = y.keys[self.t:(2 * self.t - 1)]
    y.keys = y.keys[0:self.t - 1]

    if not y.leaf:
        z.children = y.children[self.t:(2 * self.t)]
        y.children = y.children[0:self.t]

def insert_non_full(self, x, k):
    if x.leaf:
        x.keys.append(k)
        x.keys.sort()
    else:

        i = len(x.keys) - 1
        while i >= 0 and k < x.keys[i]:
            i -= 1
        i += 1

        if len(x.children[i].keys) == 2 * self.t - 1:
            self.split_child(x, i, x.children[i])
            if k > x.keys[i]:
                i += 1
            self.insert_non_full(x.children[i], k)

    def insert(self, k):
        r = self.root

        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode()
            self.root = s
            s.children.append(r)
            self.split_child(s, 0, r)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(r, k)

def search(self, k, x=None):
    if x is None:
        x = self.root
    i = 0
    while i < len(x.keys) and k > x.keys[i]:
        i += 1
    if i < len(x.keys) and k == x.keys[i]:
        return (x, i)
    elif x.leaf:
        return None
    else:
        return self.search(k, x.children[i])

    if __name__ == '__main__':
        b_tree = BTree(3)

        for i in [10, 20, 5, 6, 12, 30, 7, 17]:
            b_tree.insert(i)

        result = b_tree.search(6)
        if result:
            print(f"Chave 6 encontrada no nó: {result[0].keys}")
        else:
            print("Chave 6 não encontrada")