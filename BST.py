class Node(object): #Node 클래스 정의 
    def __init__(self, data):
        self.data = data # 노드값인 데이터 선언 
        self.left = self.right = None # 왼쪽과 오른쪽 구분 속성 선언

class BST(object):
    def __init__(self):
        self.root = None #초기의 비어있는 트리 선언 

    def insert(self, data):
        self.root = self.insert_data(self.root, data)
        return self.root

    def insert_data(self, node, data):
        if node is None:
            node = Node(data) #데이터 최초 삽입 
        else :
            if data <= node.data: #삽입되는 데이터가 작거나 같으면 왼쪽으로 삽입 
                node.left = self.insert_data(node.left, data)
            else : #삽입되는 데이터가 더 크면 오른쪽 방향으로 삽입 
                node.right = self.insert_data(node.right, data)
            return node # 노드 반환 

    def search(self, key):
        return self.sea_data(self.root, key)
        #특정 노드를 찾기 위해 키 값을 인수로 받음. 
    def sea_data(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data: # 찾는 노드가 기존 값보다 작으면 왼쪽 방향으로 검색 
            return self.sea_data(root.left, key)
        else: # 찾는 노드가 기존 값보다 크다면 오른쪽 방향으로 검색 
            return self.sea_data(root.right, key)

    def preorder(self):
        def circuit(root):
            if root is None :
                print("순회할 노드가 없습니다.")
            else :
                print(root.data)
                circuit(root.left)
                circuit(root.right)
        circuit(self.root)

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49]

bst = BST()
for x in array:
    bst.insert(x)

print(bst.search(15))
print(bst.search(17))
