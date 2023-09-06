def get_postorder(preorder, inorder, ans=""):
    if not preorder or not inorder:
        return ans
    root = preorder[0]
    index_of_root = inorder.index(root)  # 通过中序遍历找到左右子树分割点
    ans = get_postorder(preorder[1:index_of_root + 1], inorder[:index_of_root], ans)  # 左子树
    ans = get_postorder(preorder[index_of_root + 1:], inorder[index_of_root + 1:], ans)  # 右子树
    return ans + root


def main():
    preorder = input()
    inorder = input()
    postorder = get_postorder(preorder, inorder)
    print(postorder)


main()
