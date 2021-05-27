class Node(obj): #Node 클래스 정의 
    def __init__(self, data):
        self.data = data # 노드값인 데이터 선언 
        self.left = self.right = None # 왼쪽과 오른쪽 구분 속성 선언

class BST(obj):
    def __init__(self):
        self.root = None #초기의 비어있는 트리 선언 

    def insert(self, data):
        self.root = self.insert_data(self.root, data)
        return self.root

    def insert_data(self, node, data):
        if node is None:
            node = Node(data)
        else :
            if data <= node.data: #삽입되는 데이터가 작거나 같으면 왼쪽으로 삽입 
                node.left = self.insert_data(node.left, data)
            else : #삽입되는 데이터가 더 크면 오른쪽 방향으로 삽입 
                node.right = self.insert_data(node.right, data)
            return node

    def delete(self, key):
        self.root, delData = self.delete_data(self.root, key)
        return delData

    def delete_data(self, node, key):
        if node is None:
            return node, False

        delData = False
        if key == node.data;
            delData = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key<node.data:
            node.left, delData = self.delete_data(node.left, key)
        else:
            node.right, delData = self.delete_data(node.right, key)
        return node, delData

    def search(self, key):
        return self.sea_data(self.root, key)

    def sea_data(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.sea_data(root.left, key)
        else:
            return self.sea_data(root.right, key)
