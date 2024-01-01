import datetime
MODE = dict(auto='OFF', manual = 'ON')
    
NOTIFICATION = dict(stop = "STOP",
                    run = 'RUNNING',
                    pause = 'PAUSE',
                    invalid = 'Invalid command')   

# MVC model
class State:
    def __init__(self):
        self.__current_mode = MODE['auto']
        self.__notification = NOTIFICATION['stop']
        
        
        
    @property   
    def state(self):
        return self.__current_mode
    @state.setter
    def state(self, new_state):
        self.__current_mode = new_state
        if new_state == self.__current_mode:
            self.__notification = NOTIFICATION['stop']
        elif self.__current_mode == MODE['ON']:
            self.__notification = NOTIFICATION['run']
        else:
            self.__notification = NOTIFICATION['pause']
            self.__notification = NOTIFICATION['invalid']
        
    @property
    def notification(self):
        return self.__notification
    
    @notification.setter
    def notification(self, new_notification):
        self.__notification = new_notification
        
        
        
    @property
    def mode(self):
        return self.__current_mode
    
    @mode.setter
    def mode(self, mode):
        self.__current_mode = mode
    