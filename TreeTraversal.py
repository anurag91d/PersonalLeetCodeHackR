class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for i in self.children:
                i.printTree()
    def addChild(self,child):
        child.parent = self
        self.children.append(child)

def createTree():
    root = TreeNode('Vidhya')
    sravanthi = TreeNode("Sravanthi")
    sravanthi.addChild(TreeNode('Anurag'))
    sravanthi.addChild(TreeNode('Vishal'))
    sravanthi.addChild(TreeNode('Pragati'))
    sravanthi.addChild(TreeNode('Gayathri'))
    sravanthi.addChild(TreeNode('Shruti'))
    sravanthi.addChild(TreeNode('Aashi'))
    root.addChild(sravanthi)
    vinay = TreeNode("Vinay")
    vinay.addChild(TreeNode('Subham'))
    vinay.addChild(TreeNode('Ashlaan'))
    vinay.addChild(TreeNode('Siva'))
    vinay.addChild(TreeNode('Srikanth'))
    vinay.addChild(TreeNode('Amit'))
    root.addChild(vinay)
    pavan = TreeNode("Pavan")
    root.addChild(pavan)
    root.printTree()

createTree()


