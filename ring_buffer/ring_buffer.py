class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # save item to storage at current index
        self.storage[self.current] = item
        # increment current index
        self.current += 1
        # if current reaches end of storage, reset
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        # initialize a list to store return values, index at current index
        vals = []
        # loop over storage and append values, return if None is encountered
        for i in range(self.capacity):
            if self.storage[i] == None:
                return vals
            else:
                vals.append(self.storage[i])
        return vals

        # How I thought the values were supposed to be returned based on README:
        # i = self.current - 1
        # if i < 0:
        #     i = len(self.storage)
        # # loop for all possible items in storage, return if None is encountered at 0th position
        # for count in range(self.capacity):
        #     if not self.storage[i] == None:
        #         vals.append(self.storage[i])
        #     i += 1
        #     # if index reaches end of storage, reset
        #     if i == self.capacity:
        #         i = 0
        # return vals
