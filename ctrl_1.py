class Controller_1:

    def __init__(self):
        self.state = 0

    def comms(self, tp):
        
        if self.state == 0 and tp == 0:
            return 1
        
        if self.state == 2 and tp == 0:
            return 1
        
        if self.state == 1 and tp == 0:
            return 0
        

    def move(self, i, c):
        
        if self.state == 0 and i == 1 and c == 1:
            self.state = 2
            return 2
        
        if self.state == 1 and i == 0 and c == 0:
            self.state = 1
            return 3
        
        if self.state == 0 and i == 0 and c == 1:
            self.state = 0
            return 0
        
        if self.state == 2 and i == 1 and c == 0:
            self.state = 1
            return 3
        
        if self.state == 1 and i == 0 and c == 1:
            self.state = 2
            return 2
        
        if self.state == 1 and i == 1 and c == 2:
            self.state = 1
            return 3
        
        if self.state == 0 and i == 0 and c == 2:
            self.state = 1
            return 3
        
        if self.state == 2 and i == 1 and c == 1:
            self.state = 2
            return 2
        
        if self.state == 2 and i == 0 and c == 3:
            self.state = 2
            return 2
        
        if self.state == 0 and i == 1 and c == 3:
            self.state = 0
            return 0
        
        if self.state == 0 and i == 0 and c == 0:
            self.state = 1
            return 3
        
        if self.state == 2 and i == 0 and c == 2:
            self.state = 2
            return 2
        
        if self.state == 0 and i == 1 and c == 0:
            self.state = 0
            return 0
        
        if self.state == 1 and i == 0 and c == 3:
            self.state = 0
            return 0
        
        if self.state == 2 and i == 1 and c == 3:
            self.state = 1
            return 3
        
        if self.state == 1 and i == 1 and c == 1:
            self.state = 0
            return 0
        
        if self.state == 2 and i == 0 and c == 1:
            self.state = 2
            return 2
        
        if self.state == 0 and i == 0 and c == 3:
            self.state = 0
            return 0
        
        if self.state == 1 and i == 1 and c == 0:
            self.state = 0
            return 0
        
        if self.state == 2 and i == 0 and c == 0:
            self.state = 1
            return 3
        
        if self.state == 0 and i == 1 and c == 2:
            self.state = 1
            return 3
        
        if self.state == 1 and i == 1 and c == 3:
            self.state = 0
            return 0
        
        if self.state == 2 and i == 1 and c == 2:
            self.state = 0
            return 0
        
        if self.state == 1 and i == 0 and c == 2:
            self.state = 2
            return 2
        