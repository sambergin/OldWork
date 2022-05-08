
'''
Sam Bergin 170670850
Adam Joe 170801790
'''


# Import socket module
from socket import * 
import sys # In order to terminate the program
from copy import deepcopy
import threading


x = 100 #bounds for bulletin board
y = 100





class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: l = List()
        -------------------------------------------------------
        Postconditions:
            Initializes an empty list.
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = l.is_empty()
        -------------------------------------------------------
        Postconditions:
            returns
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Postconditions:
            returns
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, i, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the list at index i.
        Use: l.insert(i, value)
        -------------------------------------------------------
        Preconditions:
            i - index value (int)
            value - a data element (?)
        Postconditions:
            a copy of value is added to index i, all other values are pushed right
            If i outside of range of length of list, appended to end
        -------------------------------------------------------
        """
        if i < 0:
            # negative index
            i = self._count + i

        n = 0
        previous = None
        current = self._front

        while n < i and current is not None:
            # find the proper location in the list
            previous = current
            current = current._next
            n += 1

        if previous is None:
            # Insert a new node into the front of the list.
            self._front = _ListNode(value, self._front)
        else:
            # Insert a new node elsewhere in the list
            previous._next = _ListNode(value, current)
        self._count += 1
        return

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the list.
        Use: l.insert_front(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element. (?)
        Postconditions:
            value is added to the front of the list.
        -------------------------------------------------------
        """
        self.insert(0, value)
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        if self._front == None:
            return None,None, -1 
        
        if key == self._front.coordx:
            return None,self._front,0
        
        current = self._front
        n = 0
        previous = None
        while n < self._count and current._next is not None:

            previous = current
            current = current._next
            n += 1
            if current._coordx == key:
                return previous,current,n

        return None,None,-1
   
    


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list that matches key.
        Use: value = l.remove(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
      
        assert self._front is not None, "Cannot remove from an empty list"
       
        p,c,_ =self._linear_search(key)
        
        if c ==None:
            value = None
        else:
            value = c._value
            self.remove_front()
        
            if p == None:
                self._front = c._next
            
            else:
                p._next = c._next
            
        
        
        self._count -= 1

        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = l.remove_front()
        -------------------------------------------------------
        Postconditions:
            returns
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._data
        self._front = self._front._next
        self._count -= 1
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Preconditions:
            key - a data element (?)
        Postconditions:
            Removes all values matching key.
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        current = self._front
        
        if current == None:
            return 
        
        while current != None:
            if current._data==key:
                if current ==self._front:
                    self.remove_front()
                    current = current._next
                else:   
                    self.remove(key)
                    current = current._next  
            else:
                #print(current._data)
                
                current = current._next
        
        return
        
        
        


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _,value,_ =self._linear_search(key)
        

        return value

    
    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        _,_,i =self._linear_search(key)


        return i

    

    
    
    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """

        _,c,_ =self._linear_search(key)

        return c is not None

    
    
    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = l.count(key)
        -------------------------------------------------------
        Preconditions:
            key - a partial data element (?)
        Postconditions:
            returns
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """

        number = 0
        current = self._front

        while current is not None:
            if key == current._data:
                number += 1
            current = current._next
        return number

    # return number

    def append(self,coordx,coordy, width, height, color, msg):
        """
        ---------------------------------------------------------
        Appends a copy of value to the end of the List.
        Use: l.append(value)
        -------------------------------------------------------
        Preconditions:
            value - a data element (?)
        Postconditions:
            a copy of value is added to the end of the List.
        -------------------------------------------------------
        """
        note = Note()
        note.new_note(coordx,coordy, width, height, color, msg, None)
       
        if self._front == None:
            self._front = note
            
            
        else:
            current = self._front
            while current._next is not None:
                current = current._next
            current._next = note
       

        return

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (iterative algorithm)
        Use: l.clean()
        -------------------------------------------------------
        Postconditions:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """

        cleaned = []
        
        if self._front == None:
            return
        current = self._front
        i = 0
        while current != None:
            #print(cleaned)
            if current._data in cleaned:
                
                current = current._next
                self.pop(i)
                
            else:
                cleaned.append(current._data)
                i = i +1
                current = current._next

        return

    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.remove(i)
        -------------------------------------------------------
        Preconditions:
            i - an array of arguments (?)
                i[0], if it exists, is the index
        Postconditions:
            returns
            value - if i exists, the value at position i, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                i[0] = self._count + i[0]
            j = 0

            while j < i[0]:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._data

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Postconditions:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current
            current = current._next
            
    def clear(self):
        cleared = 0
        for i in self:
            if i.status == 0:
                coord = [int(i.coordx),int(i.coordy)]
                self.remove(coord)
                cleared+=1
        return cleared
        
                
            


class _ListNode:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node.
        Use: node = _ListNode(value, _next)
        -------------------------------------------------------
        Preconditions:
            _data - data value for node (?)
            _next - another list node (_ListNode)
        Postconditions:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._data = deepcopy(value)
        self._next = next_
        return

class Note:
    def __init__(self):
        self.coordx = 0
        self.coordy = 0
        self.width = 0
        self.height = 0
        self.color = None
        self.msg = None
        self.status = 0
        self._next = None
        
    def set_coord(self, coordx, coordy):
        self.coordx = coordx
        self.coordy = coordy
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self,height):
        self.height = height
        
    def set_color(self,color):
        self.color = color
        
    def set_msg(self, msg):
        self.msg = msg
        
    def set_status(self,status):
        self.status = status
        
    def to_string(self):
        print(self.coordx, self.coordy)
        print(self.width)
        print(self.height)
        print(self.msg)
        print(self.status)
    def new_note(self,coordx,coordy, width, height, color, msg, n):
        self.coordx = coordx
        self.coordy = coordy
        self.width = width
        self.height = height
        self.color = color
        self.msg = msg
        self.status = 0
        self._next = n


dic = List()
class ClientThread(threading.Thread):
    def __init__(self,clientsocket):
        threading.Thread.__init__(self)
        self.connectionSocket = clientsocket
        print ("New connection added")
    def run(self):
        
        
        msg = ''
        while True:
            print('The server is ready to receive')
    
    
            
            
        
            post = self.connectionSocket.recv(1024)
            post2 = post.decode()
            data = Convert(post2)
                
            
            
            
                
            if data[0] == '3':
                    
                    
                    
                dic.append(data[1], data[2], data[3], data[4], data[5], data[6])
                    
                ms = "This note has been added."
                    
                self.connectionSocket.send(ms.encode())
                    
                
            elif data[0] == '2':
                print("client disconnected")
                self.connectionSocket.close()
                    
                    
            elif data[0] == '4':
                    
                if data[1] != 'None' and data[2] != 'None' and data[3] != 'None' and data[4] != 'None':
                    for i in dic:
                        
                        if i.coordx == data[1]:
                            if i.coordy == data[2]:
                                if i.color == data[3]:
                                    if data[4] in i.msg:
                                        notmsg = ""
                                        notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " + i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                    
                                        self.connectionSocket.send(notmsg.encode())
                            
                elif data[1] != 'None' and data[2] != 'None' and data[3] != 'None' and data[4] == 'None':
                    for i in dic:
                        
                        if i.coordx == data[1]:
                            if i.coordy == data[2]:
                                if i.color == data[3]:
                                    notmsg = ""
                                    notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                    
                                    self.connectionSocket.send(notmsg.encode())
                            
            
                elif data[1] != 'None' and data[2] != 'None' and data[3] == 'None' and data[4] != 'None':
                    for i in dic:
                        if i.coordx == data[1]:
                            if i.coordy == data[2]:
                                if data[4] in i.msg:
                                    notmsg = ""
                                    notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " + i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                    
                                    self.connectionSocket.send(notmsg.encode())
                            
                elif data[1] != 'None' and data[2] != 'None' and data[3] == 'None' and data[4] == 'None':
                    for i in dic:
                        if i.coordx == data[1]:
                            if i.coordy == data[2]:
                                notmsg = ""
                                notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                    
                                self.connectionSocket.send(notmsg.encode())
                            
                elif data[1] == 'None' and data[2] == 'None' and data[3] != 'None' and data[4] != 'None':
                    for i in dic:
                        if i.color == data[3]:
                            if data[4] in i.msg:
                                notmsg = ""
                                notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " + i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                        
                                self.connectionSocket.send(notmsg.encode())
                        
                elif data[1] == 'None' and data[2] == 'None' and data[3] != 'None' and data[4] == 'None':
                    for i in dic:
                        if i.color == data[3]:
                                
                            notmsg = ""
                            notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                        
                            self.connectionSocket.send(notmsg.encode())
                            
                elif data[1] == 'None' and data[2] == 'None' and data[3] == 'None' and data[4] != 'None':
                    for i in dic:
                            
                        if data[4] in i.msg:
                                
                            notmsg = ""
                            notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status)+ " " + 'has been retrieved'
                                                        
                            self.connectionSocket.send(notmsg.encode())
                            
                elif (data[1] != 'None' and data[2] == 'None') or (data[1] == 'None' and data[2] != 'None'):
                    notmsg = 'invalid coordinates.'
                    self.connectionSocket.send(notmsg.encode())
                    
                elif(data[1] == 'PINS'):
                    for i in dic:
                        if i.status ==1:
                            notmsg = ""
                            notmsg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status) + " " + 'has been retrieved'
                                                        
                            self.connectionSocket.send(notmsg.encode())
                                
                        
            elif data[0] == '5':
                for i in dic:
                    if i.coordx == data[1] and i.coordy == data[2]:
                        i.set_status(1)
                        msg = ""
                        msg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status) + " " + 'has been pinned'
                        self.connectionSocket.send(msg.encode())
                
            elif data[0] == '6':
                for i in dic:
                    if i.coordx == data[1] and i.coordy == data[2]:
                        i.set_status(0)
                        msg = ""
                        msg += i.coordx + " " + i.coordy + " " + i.width + " " +i.height + " " + i.color + " " +i.msg +" "+str(i.status) + " " + 'has been unpinned'
                        self.connectionSocket.send(msg.encode())
                            
            elif data[0] == '7':
                msg = dic.clear()
                msg2 = str(msg) + " " + 'notes have been cleared'
                self.connectionSocket.send(msg2.encode())            
        
                
        
        
        
        
        
                    
      
        
def Convert(s):
    l = list(s.split(" "))
    return l
def list2str(d):
    str2 = " "
            
    return str2.join(d)



LOCALHOST = "127.0.0.1"
PORT = 8080
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
s.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")        
while True:
    s.listen(1)
    connectionSocket, _ = s.accept()
    newthread = ClientThread(connectionSocket)
    newthread.start()

connectionSocket.close()



s.close()  
sys.exit()


    

        
