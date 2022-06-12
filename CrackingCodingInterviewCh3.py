
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 3 - Stacks and Queues'''


# 3.1 - Three in One
# Describe how you could use a single array to implement three stacks. 

""" Java Solution """

""" 
public class ThreeStacks {
    public int capacity;
    public int numberStacks = 3;
    public int[] values;
    public int[] sizes; 
    
    //Constructor
    public ThreeStacks(int size){
        this.values = new int[size * numberStacks];
        this.sizes = new int[numberStacks];
        this.capacity = size; 
    }

    //Push values into the stack 
    public void push(int stackNum, int item) throws FullStackException{
        
        //If stack is full, throw a FullStackException
        if isFull(stackNum){
            throw new FullStackException(); 
        }

        //Add item to the stack
        sizes[stackNum]++; 
        values[indexAtTop(stackNum)] = item; 

    }

    //Remove the first value from the stack
    public int pop(int stackNumber) throws EmptyStackException {
        
        //If stack is empty, throw EmptyStackException 
        if isEmpty(stackNum){
            throw new EmptyStackException(); 
        }

        int item = values[indexAtTop(stackNum)];
        values[indexAtTop(stackNum)] = 0; 
        this.sizes[stackNum]--; 

        return item; 
    }

    //Return the top element of the stack
    public int peek(int stackNumber) throws EmptyStackException{
        //If stack is empty, throw EmptyStackException 
        if isEmpty(stackNum){
            throw new EmptyStackException(); 
        }

        //Return the top element 
        return values[indexAtTop(stackNum)]; 

    }

    //Return if the stack is empty
    public boolean isEmpty(int stackNumber){
        return sizes[stackNum] == 0; 
    }

    //Return if the stack is full
    public boolean isFull(int stackNumber){
        return sizes[stackNum] == capacity;
    }

    //Check the index at the top of the current stack
    private int indexAtTop(int stackNumber){
        int offset = stackNumber * this.numberStacks; 
        int currentSize = sizes[stackNumber]
        
        return offset + currentSize - 1; 
    }
}

"""

# 3.2 - Stack Min
# Design a stack which contains the function min() which returns the minimum element. 
# This is in addition to the push and pop functions. 
# Push, pop, and min functions should all operate in O(1) time. 

class StackMod: 
    def __init__(self): 
        self.stack = []
        self.minimum = []
    
    def push(self, item): 
        if (self.minimum[-1] == None) or (self.minimum[-1] > item): 
            self.minimum.append(item) 
            
        self.stack.append(item)

    def pop(self): 
        item = self.stack.pop()

        if (item == min()): 
            self.minimum.pop() 

        return item
    
    def peek(self): 
        return self.minimum[-1]

    def min(self):
        if (len(self.minimum) == 0): 
            return None

        return self.peek()

# 3.3 - Stack of Plates
# Imagine a (literal) stack of plates. If the stack is too high, it might topple. 
# The goal is to start a new stack when the previous stack exceeds some threshold. 
# This data structure, SetofStacks, should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 
# The push() and pop() should behave identically to a single stack. 

class Stack:
    CAPACITY_LIMIT = 10 
    
    def __init__(self): 
        self.stack = []
    
    def push(self, item): 
        self.stack.append(item) 
    
    def pop(self): 
        return self.stack.pop() 
    
    def peek(self): 
        return self.stack[-1]
    
    def isEmpty(self): 
        return len(self.stack) == 0

class SetofStacks: 
    stacks = [] #A list of stacks

    def push(self, value): 
        pass
    
    def pop(self): 
        pass

# FOLLOW-UP: Implement a function popAt() which performs a pop operation on a specific substack.