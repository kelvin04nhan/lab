from model.state import State

MODE = dict(auto='OFF', manual = 'ON')
    
NOTIFICATION = dict(stop = "STOP",
                    run = 'RUNNING',
                    pause = 'PAUSE',
                    invalid = 'Invalid command')   

class Engine:
    def __init__(self, washer):
        self.state = State()
        self.washer = washer
        
    def start_engine(self, new_mode):
        self.state.mode = MODE[new_mode]
        
    def end_engine(self):
        self.state.mode = MODE['auto']
        
    def change_mode(self):
        mode = self.state.mode()
        if mode == MODE['auto']:
            mode = MODE['manual']
            
        elif mode == MODE['manual']:
            mode = MODE['auto']
            
        self.state.mode(mode)
        
    def update_odometer(self):
        self.washer.display_menu()