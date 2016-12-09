#coding:utf-8

data=[1,2,3,4,5,6,7]

class Node():
        def __init__(self,value):
		self.node_count=0
	        self.left=None
                self.right=None
                self.partent=None
                self.value=value

def generate(data):
        if len(data)==0:return
        root=Node(data[0])
	root.node_count+=1
        for i in range(1,len(data):

                
def addNode(value,root):
        node=root
        while(True):
                if node.left == None:
                        new_node=Node(i)
                        new_node.partent = node
                        node.left = new_node
                	root.node_count+=1 
		       continue
                elif node.right = None:
                        new_node=Node(i)
                        new_node.partent = node
                        node.left = new_node
			root.node_count+=1
                        continue
		
                node = node.left
                      

generate(data)
