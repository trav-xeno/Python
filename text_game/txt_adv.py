'''
yeild use in a generator function 
_varName  protected 
__varName  private 
'''
import re,math,random
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class adv:
    __level = [0,1,2,3,4,5,6,7]
    __success = []
    __fails = []
    __name = ""

    def __checkInput(self, st):
        check_string = re.compile("[^a-zA-Z]")
        if check_string.search(st) == None:
            return False
        else:
            return True
    
    def __intro(self ):
        uIn = input("Enter your name: ")
        while True:
            if self.__checkInput(uIn):
                uIn = input("Enter letters plase no numbers or specail characters: " )
            else:
                break

        greeting = "Hello, " + self.__name 
        print(greeting)
        print("""Welcome to purgatory!
        Your fate has not been decided yet...Well, more likely we lost your applicaiton and are currently trying to find it. 
        But hey you can help out in the mean time!
        """)
    ''' 
    starts creates the loop read the yaml file for saved states and starts off/generates the decision trees for the story. 
    based on past actions
    '''

    def start(self):
        if self.__level[0] == 0:
            self.__intro()
        
''' 
this class will read and save state of game 
'''
class GameConfig:
    __configure = "./config.yaml"
    def getSaveState(self):
        #get yaml file parse to get saves and leve data related
        pass
    def getDesTree(self):
        # return the the tree they have done so far  and whats left based on past decisions
        pass
    def save(self,phase):
        #takes current phase and updates gameconfig.yaml
        pass

def main():
    game = adv()
    game.start()

if __name__ == "__main__":
    main()