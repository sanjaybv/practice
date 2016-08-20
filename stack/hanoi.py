class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.stack_1 = range(num_disks)
        self.stack_2 = []
        self.stack_3 = []

    def run(self):
        self.move(self.num_disks, self.stack_1, self.stack_2, self.stack_3)

    def move(self, n, src, dest, buff):
        if not n:
            return
        self.move(n-1, src, buff, dest)
        dest.append(src.pop())
        self.move(n-1, buff, dest, src)
        print self

    def __repr__(self):
        return 'stack 1: {0}\nstack 2: {1}\nstack 3: {2}\n'\
                .format(self.stack_1, self.stack_2, self.stack_3)

if __name__ == '__main__':
    t = TowerOfHanoi(5)
    print t
    t.run()
