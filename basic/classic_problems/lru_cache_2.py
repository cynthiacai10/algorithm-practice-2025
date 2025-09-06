class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {} # key -> node

        # Dummy head & tail
        self.head = Node(0, 0)   # least recently used is right after head
        self.tail = Node(0, 0)   # most recently used is right before tail
        self.head.next = self.tail
        self.tail.prev = self.head

   # --- Doubly linked list helpers ---
    def _remove(self, node: Node):
        """Detach node from list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_tail(self, node: Node):
        """Insert node right before tail (MRU position)."""
        # connect with previous tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev

        # make node new tail
        node.next = self.tail
        self.tail.prev = node

    # --- Public API ---
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._remove(node)
        self._add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node: # update old node
            node = self.key_to_node[key]
            node.val = value
            self._remove(node)
            self._add_to_tail(node)
        else: # add new node
            if len(self.key_to_node) == self.capacity:
                # evict LRU (node right after dummy head)
                evicted = self.head.next
                self._remove(evicted)
                self.key_to_node.pop(evicted.key)
            new_node = Node(key, value)
            self._add_to_tail(new_node)
            self.key_to_node[key] = new_node

    def show_cache(self):
        cache_list = []
        for key, values in self.key_to_node.items():
            cache_list.append((key, values.val))
        print("all cache:",cache_list)
        print("======")

def test1():
    lrucache = LRUCache(2)
    lrucache.put(1, 10)  # cache: {1=10}
    lrucache.get(1)      # return 10
    lrucache.put(2, 20)  # cache: {1=10, 2=20}
    lrucache.put(3, 30)  # cache: {2=20, 3=30}, key=1 was evicted
    lrucache.get(2)      # returns 20
    lrucache.get(1)      # return -1 (not found)


def test2():
    lrucache = LRUCache(2)
    lrucache.put(1, 1) # cache: {1=1}
    lrucache.put(2, 2) # cache: {1=1, 2=2}
    lrucache.get(1)    # return 1
    lrucache.put(3, 3) # cache: {1=1, 3=3}
    lrucache.get(2)    # return -1
    lrucache.put(4, 4) # cache: {3=3, 4=4}
    lrucache.get(1)    # return -1
    lrucache.get(3)    # return 3
    lrucache.get(4)    # return 4

if __name__ == "__main__":
    test1()