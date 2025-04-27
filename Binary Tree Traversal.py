class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):

    if node is None:
        return []

    stack = [node]
    result = []

    while stack:
        current = stack.pop()
        result.append(current.data)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    return result


# In-order traversal
def in_order(node):

    result = []
    stack = []
    current = node

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right

    return result
#[10] should equal [10, 5, 'leaf', 2]
# Test Passed
# ['leaf'] should equal ['leaf', 2]

# test.assert_equals(in_order(a), [b.data, a.data, d.data, c.data])
# test.assert_equals(in_order(b), [b.data])
# test.assert_equals(in_order(c), [d.data, c.data])

# Post-order traversal
def post_order(node):
    if node is None:
        return []

    stack = [node]
    result = []

    while stack:
        current = stack.pop()
        result.append(current.data)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result[::-1]

a = Node(5)
b = Node(10)
c = Node(2)
d = Node("leaf")
a.left = b
a.right = c
c.left = d

pre_order(a) # [5, 10, 2, "leaf"]
in_order(a)
@test.it('Pre-order Tests')
def pre_order_tests():
    test.assert_equals(pre_order(a), [a.data, b.data, c.data, d.data])
    test.assert_equals(pre_order(b), [b.data])
    test.assert_equals(pre_order(c), [c.data, d.data])

@test.it('In-order Tests')
def in_order_tests():
    test.assert_equals(in_order(a), [b.data, a.data, d.data, c.data])
    test.assert_equals(in_order(b), [b.data])
    test.assert_equals(in_order(c), [d.data, c.data])

@test.it('Post-order Tests')
def post_order_tests():
    test.assert_equals(post_order(a), [b.data, d.data, c.data, a.data])
    test.assert_equals(post_order(b), [b.data])
    test.assert_equals(post_order(c), [d.data, c.data])
    
@test.it('Empty Node Tests')
def None_tests():
    test.assert_equals(pre_order(None), [])
    test.assert_equals(in_order(None), [])
    test.assert_equals(post_order(None), [])