class node:
    
    #a node basic next and current value of data ans posi
      def __init__(self,data):#initally no data
          self.data=data
          self.next=None
# a singlly  linked list would be ssociated from a head to  tail with  a position and data it is referring to          
class LinkedList:
    def __init__(self):
        self.head=None

    #initiates a node
    #adds new data to  end of current linked list
    def  append(self,data):
        new_node=node(data)
        #when no entries are there at all
        if self.head==None:
            self.head=new_node
            return
            #if some nodes already exists we need to get to the end of the link list (till next gives null0)
        last_node=self.head
        while last_node.next:#is not null
            last_node=last_node.next
        last_node.next=new_node
    def print_list(self):
        current_node=self.head
        while current_node.next!=None:
            print(current_node.data)
            current_node=current_node.next
    def prepend(self,data):                          #first make a new node
        new_node=node(data)                          #link ir with preset  head                        
        new_node.next=self.head                       #turn new node into  a head              
        self.head=new_node
    def insert(self,previous_node,data):
        if not previous_node: #IF  ENTERD PREVISIOUS NODE DPESNT EXIST IN OUT DATA                       #inserting in betwen particular [position nodes]           
            print("Previous node enterd doesn't exist")
            return 
        #if previous node entered does exist  
        new_node=node(data)
        new_node.next=previous_node.next#assign the next  of new item as next  of previous item
        previous_node.next=new_node# take plece bn prev and neaxt item as  a node
        
        
    ######################################DELETING##################################################

    def delete_node(self,key):
        current_node=self.head
        if current_node and current_node.data==key:#if list is not empty AND  currrent node data is equal to  key
            self.head=current_node.next#only one node is there deelete that and give next node as head
            current_node=None#delete current node
            return
            ####list exists and now need to  check all elements for given key
        previous_node=None# to  find refernce neighbour nodes of subject node
        while current_node and current_node.data!=key: #current node doest refer to  null and traverse untill find the node with desired value
            previous_node=current_node#head is not the the key node andkeep checking making it previous
            current_node=current_node.next#check for next node 
        if current_node is None:##if given data doesnt exist in list then after traversing would point to  null
            return
    #in case the current node is found which holds the esired data ie key
        previous_node.next=current_node.next#link the neighbours
        current_node=None#delete the fiund node with key value
    ####################deleting by position##############################################################
    def  delete_position(self,position):
        current_node=self.head
        if  position==0:#if the head or 0  position is enterd lets take it as  edge case
            self.head=current_node.next#make next node the head
            current_node=None#clear the node
            return
        previous_node=None
        count=1#becoze 0  is edge case
        while current_node and  count!=position:#traverse through list from head-current node to  the count of desired position 
            previous_node=current_node#left hand side neighbpout
            current_node=current_node.next#the node we desire and next to  traverse in list
            count+=1#posi count
        if current_node is None:#after the wholw traversing if we dont find any current node with refernce to  posi and node becomes null
            return
        previous_node.next=current_node.next#iff found then left side-previous link to  the right side neighbour
        current_node=None#and the posi is cleared
    #######################################LENGTH############################################################
    def length_len(self):
        current_node=self.head
        count=0
        while current_node :
            count+=1
            current_node=current_node.next
        print(count)
        return count
    
    

            
    




         







        
        
