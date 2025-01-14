# 코드 미완성 , 완성 해야함 [ ] 
tree = ["a","b","c","d","e","f",None,"g"]
def preorder(tree,i=0):
    # 3개를 다 돌면 끝난다
    # left / right 로 나눠야 함 
    
    output = [tree[i]]
    left = 2 * i + 1
    right = left + 1
    if left < len(tree) and tree[left] is not None:
        output += preorder(tree, left)
    if right < len(tree) and tree[right] is not None:
        output += preorder(tree, right)
    return output
print(preorder(tree))