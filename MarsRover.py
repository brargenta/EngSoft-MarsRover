class MarsRover:
    def __init__(self, file):
        self.x_size = 0
        self.y_size = 0
        self.x_start = []
        self.y_start = []
        self.x_current = []
        self.y_current = []
        self.orientation = []
        self.movements = []
        self.read_file(file)

    def read_file(self, file):
        f = open(file, "r")
        cont_line = 0
        self.cont_rover = 0
        temp = [line.rstrip('\n') for line in f]
        for line in temp:
            if line != '':
                cont_line += 1
                if cont_line == 1:
                    list = line.split(" ")
                    self.x_size, self.y_size = int(list[0]), int(list[1])
                elif cont_line == 2:
                    list = line.split(" ")
                    x_start, y_start = int(list[0]), int(list[1])
                    self.x_start.append(x_start)
                    self.y_start.append(y_start)
                    self.orientation.append(list[2])
                    self.x_current.append(x_start)
                    self.y_current.append(y_start)            
                elif cont_line == 3:
                    self.movements.append(line)
                    self.cont_rover += 1
                    cont_line = 1
        f.close()
    def rotate_rover(self, rover, movement):
        if(self.orientation[rover] == "N"):
            if(movement == "L"):
                self.orientation[rover] = "W"
            elif(movement == "R"):
                self.orientation[rover] = "E"
        elif(self.orientation[rover] == "S"):
            if(movement == "L"):
                self.orientation[rover] = "E"
            elif(movement == "R"):
                self.orientation[rover] = "W"
        elif(self.orientation[rover] == "E"):
            if(movement == "L"):
                self.orientation[rover] = "N"
            elif(movement == "R"):
                self.orientation[rover] = "S"
        elif(self.orientation[rover] == "W"):
            if(movement == "L"):
                self.orientation[rover] = "S"
            elif(movement == "R"):
                self.orientation[rover] = "N"
    def move_rover(self, rover):
        if(self.orientation[rover] == "N"):
            if(self.y_current[rover] < self.y_size):
                self.y_current[rover] += 1
        elif(self.orientation[rover] == "S"):
            if(self.y_current[rover] > 0):
                self.y_current[rover] -= 1
        elif(self.orientation[rover] == "E"):
            if(self.x_current[rover] < self.x_size):
                self.x_current[rover] += 1
        elif(self.orientation[rover] == "W"):
            if(self.x_current[rover] > 0):
                self.x_current[rover] -= 1
    def start(self):
        for iter in range(0, self.cont_rover):
            for movement in self.movements[iter]:
                if(movement == "M"):       
                    self.move_rover(iter)
                else:
                    self.rotate_rover(iter, movement)
            print(str(self.x_current[iter]) + " " + str(self.y_current[iter]) + " " + str(self.orientation[iter]))
MarsRover("test_input.txt").start()