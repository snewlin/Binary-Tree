#Lab #7
#Due Date: 07/25/2021, 11:59PM 

class MinPriorityQueue:
    '''
        >>> h = MinPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        return self._heap[0]
        pass
    
    
    def _parent(self,index):
        if index<=1:
            return None         #index goes in as heaplist format, changed to pylist format with formula to identify value
        else:
            return self._heap[(index//2) -1] #output parent value
        pass

    def _leftChild(self,index):         #goes in as heaplist, changed to pylist format with formula to identify value
        if (index*2-1) <=(len(self._heap)-1):
            return self._heap[index*2 -1]   #output leftchild value
        pass


    def _rightChild(self,index):        #goes in as heaplist, changed to pylist format with formula to identify value
        if (index*2)<=(len(self._heap)-1):
            return self._heap[index*2]      #output rightchild value
        pass


    def insert(self,item):
        self._heap.append(item)         #adding item to list
        itemind=len(self._heap)       #identifying the items pylist index
        #if the pylist index is 0, no parents so nothing is done
        #while loop continues if the parent of the item index(add one to adjust to heap list format)
        #is greater than the value at the item index
        while (self._parent(itemind) is not None) and (self._parent(itemind) > self._heap[itemind-1]):
            #remembering the parent value 
            rem=self._heap[itemind-1]
            #making the value at the parent's index equal to item
            self._heap[itemind-1]=self._heap[itemind//2 -1]
            #making the value at the original index equal to the parent value (swapping them)
            self._heap[itemind//2 -1]=rem
            #updating the item index to the parent index
            itemind=(itemind//2)
            

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            x=self._heap[0]
            self._heap=[]
            return x
        else:
            #storing the value moved to the top
            rem=self._heap[len(self._heap)-1]
            #storing return value for minimum
            x=self._heap[0]
            #popping last element
            self._heap.pop()
            #moving last element to the root
            self._heap[0]=rem
            #initializing the index of the value moving down
            i=1
            #checking that the children are either both less than i, one is and one isnt, or one is and one is none
            while (self._leftChild(i) is not None and self._leftChild(i)<self._heap[i-1]) or (self._rightChild(i) is not None and self._rightChild(i)<self._heap[i-1]):
                #if the leftchild is not none and less than its parent, they are swapped
                #if the left and right are less than its parent, the smallest is swapped
                #if the left and right child are equal and less than their parent, the left child is swapped with the parent
                if (self._leftChild(i) is not None and self._leftChild(i)<self._heap[i-1]) and (self._rightChild(i) is None or self._leftChild(i)<=self._rightChild(i)):
                    l=self._leftChild(i)
                    self._heap[i*2 -1]=self._heap[i-1]
                    self._heap[i-1]=l
                    i=i*2
                #i is decreased based on which child is swapped to continue trickling down until the while loop doesnt apply
                elif (self._rightChild(i) is not None and self._rightChild(i)<self._heap[i-1]) and (self._leftChild(i) is None or self._leftChild(i)>self._rightChild(i)):
                    r=self._rightChild(i)
                    self._heap[i*2]=self._heap[i-1]
                    self._heap[i-1]=r
                    i=i*2+1

            #returning the minimum that was popped
            return x

        
        
            pass



def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    #creating min heap object
    x=MinPriorityQueue()
    #initializing empty list for sorted values
    sortlst=[]
    #adding values from the numList into the heap
    for i in numList:
        x.insert(i)
    #looping deleteMin attribute to return the minimum of the heap and add to empty list until the heap is empty
    for j in range(len(x._heap)):
        sortlst.append(x.deleteMin())
    #returning sorted list
    return sortlst
if __name__=='__main__':
    import doctest
    doctest.testmod()     
