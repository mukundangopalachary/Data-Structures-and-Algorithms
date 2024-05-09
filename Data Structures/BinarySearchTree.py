class Binarysearchtree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if data == self.data:
            return "Data exists."
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binarysearchtree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binarysearchtree(data)        
                
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
            
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
            
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        
        return elements
        
    def pre_order_transversal(self):
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_transversal()
        
        if self.right:
            elements += self.right.pre_order_transversal()
            
        return elements
    
    def calculate_sum(self):
        Sum = 0
        elements = self.in_order_traversal()
        Sum = sum(elements)
        
        return Sum
    
    def min(self):              #0(1)
       elements = self.in_order_traversal()
       
       return elements[0]
    
    def max(self):              #0(1)
        elements = self.in_order_traversal
        
        return elements[-1]
               
    def search(self, val):      #0(log(n)) for searching 
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
                
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
            
            
    
def build_tree(elements):
    root = Binarysearchtree(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = []                #Enter the values
    numbers_tree = build_tree(numbers)