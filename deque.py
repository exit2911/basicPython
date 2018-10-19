# deque objects are like double-ended queues

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    
    print("THIS IS",d)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop() #last element
    
    
    d.popleft() #most left element
    d.append(2) #add 2 to the right
    d.appendleft(1) #add 1 to the left
    print(d) #print d which was done some operations on

    # rotate the deque
    print(d)
    d.rotate(1) #rotate
    print(d)


if __name__ == "__main__":
    main()
