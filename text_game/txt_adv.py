'''
yeild use in a generator function 
_varName  protected 
__varName  private 
'''
class adv:
    level = [1,2,3,4,5,6,7]
    __success = []
    __fails = []
     
    def __init__(self, name):
        self.name = name
    def start(self):
        greeting = "Hello, " + self.name 
        print(greeting)
        print("""Welcome to purgatory!
        Your fate has not been decided yet...Well, more likely we lost your applicaiton and are currently trying to find it. 
        But hey you can help out in the mena time!
        """)

def main():
    uIn = input("Enter your name: ")      
    game = adv(uIn)
    game.start()

if __name__ == "__main__":
    main()