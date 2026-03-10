def dfs(tree, words):

    node = tree

    for word in words:

        if isinstance(node, dict) and word in node:
            node = node[word]
        else:
            return None

    if isinstance(node, str):
        return node

    return None