class animal:
    def __init__(self, line=None):
        if line:
            self.line = line
        else:
            self.line = 'I am an animal'

    def say(self):
        print line

class dog(animal):
    def say(self):
        super.say()

if __name__ == '__main__':
    d = dog()
    d.say()
