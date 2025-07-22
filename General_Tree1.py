class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print_tree(self):
        spaces=' ' * self.get_level()*3
        prefix = spaces + "|___" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)


def build_management_tree():
        root1=TreeNode("CEO")

        CTO=TreeNode("CTO")
        Infrastructure_Head=TreeNode("Infrastructure Head")
        Infrastructure_Head.add_child(TreeNode("Cloud Manager"))
        Infrastructure_Head.add_child(TreeNode("App Manager"))

        Application_Head=TreeNode("Application Head")

        HR_Head=TreeNode("HR Head")
        HR_Head.add_child(TreeNode("Recruitment Manager"))
        HR_Head.add_child(TreeNode("Policy Manager"))

        root2=TreeNode("Nilupul")

        Chinmay=TreeNode("Chinmay")

        Vishwa=TreeNode("Vishwa")
        Vishwa.add_child(TreeNode("Dhaval"))
        Vishwa.add_child(TreeNode("Abhijit"))

        Aamir=TreeNode("Aamir")
        Gels=TreeNode("Gels")
        Gels.add_child(TreeNode("Peter"))
        Gels.add_child(TreeNode("Waqas"))

        root1.add_child(CTO)
        CTO.add_child(Infrastructure_Head)
        CTO.add_child(Application_Head)
        root1.add_child(HR_Head)
        
        root2.add_child(Chinmay)
        Chinmay.add_child(Vishwa)
        Chinmay.add_child(Aamir)
        root2.add_child(Gels)
      
        root1.print_tree()
        root2.print_tree()



if __name__ == '__main__':
    root_node = build_management_tree()
    # root_node.print_tree("name") # prints only name hierarchy
    # root_node.print_tree("designation") # prints only designation hierarchy
    # root_node.print_tree("both") # prints both (name and designation) hierarchy