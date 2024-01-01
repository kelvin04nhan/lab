from view.washer import Washer
class Simulator:
    def __init__(self):
        self.washer = Washer()
        
    def run(self):
        while True:
            self.__washer.display_menu()
            choice = input("Enter your command: ")
            for command in choice:
                if command == '0':
                    return 
                self.process_menu(command)
                
                
    def process_menu(self, command):
        if command == '1':
            self.washer.start_engine() 
            
        elif command == '2':
            self.washer.end_engine()
        elif command == '3':
            self.washer.change_mode()
            
            
        else:
            pass
        
def main():
    simulator = Simulator()
    simulator.run()
    
    
if __name__ == '__main__':
    main()   
            
            