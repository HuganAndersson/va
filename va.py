import tkinter as tk
import math

ball_size = 20
friction = 0.1
ball_amount = 2
player_amount = 1
angle = 0
ball_lst =[]
colors = ["blue","yellow","black"]

class Ball:
    def __init__(self,coordinates,color,canvas):
        self.speed_x=0
        self.speed_y=0
        self.coordinates = coordinates
        self.color = color
        x = self.coordinates[0]
        y = self.coordinates[1]
        self.ball = canvas.create_oval(x-(ball_size//2),y-(ball_size//2),x+(ball_size//2),y+(ball_size//2),fill=color,tag=self.color)

    def get_coordinates(self):
        return self.coordinates

    def move(self,canvas,new_speed,window):
        self.speed_x=new_speed[0]
        self.speed_y=new_speed[1]
        canvas.move(self.color,self.speed_x,self.speed_y)

        if math.isclose(self.speed_x,0,abs_tol=0.00001) == False:
            if abs(self.speed_x) < friction:
                self.speed_x = 0
            elif self.speed_x > 0:
                self.speed_x = self.speed_x-friction
            elif self.speed_x < 0:
                self.speed_x = self.speed_x+friction
        if math.isclose(self.speed_y,0,abs_tol=0.000001) == False:
            if abs(self.speed_y) < friction:
                self.speed_y = 0

            elif self.speed_y > 0:
                self.speed_y -= friction
            elif self.speed_y < 0:
                self.speed_y += friction

        new_speed =(self.speed_x,self.speed_y)
        self.coordinates = (self.coordinates[0]+self.speed_x,self.coordinates[1]+self.speed_y)
        print(self.coordinates)
        
        if  math.isclose(self.speed_x,0,abs_tol=0.00001) == False or math.isclose(self.speed_y,0,abs_tol=0.00001) == False:
            window.after(1, self.move(canvas,new_speed,window))

        

        
        #canvas.move(self.color,new_coordinates[0],new_coordinates[1])
        
        



        


class Que:
    def __init__(self,coordinates,angle,canvas):
        self.angle = angle
        self.theta = math.radians(self.angle)
        self.radius = ball_size//2
        self.coordinates = coordinates
        self.que = canvas.create_line(coordinates[0]+self.radius*math.cos(self.theta),coordinates[1]+self.radius*math.sin(self.theta),
                           coordinates[0]+self.radius*(math.cos(self.theta)*10),coordinates[1]+self.radius*(math.sin(self.theta)*10),fill="black",arrow = tk.LAST,tags="que")
        
    def move_que(self,angle,canvas):
        self.angle = self.angle+angle
        self.theta = math.radians(self.angle)
        canvas.delete(self.que)
        self.que = canvas.create_line(self.coordinates[0]+self.radius*math.cos(self.theta),self.coordinates[1]+self.radius*math.sin(self.theta),
                           self.coordinates[0]+self.radius*(math.cos(self.theta)*10),self.coordinates[1]+self.radius*(math.sin(self.theta)*10),fill="black",arrow = tk.LAST,tags="que")
        
    #def move_withball(self,new_coordinates,canvas):
            #canvas.delete(self.que)
            #self.coordinates = new_coordinates
           # self.que = canvas.create_line(self.coordinates[0]+self.radius*math.cos(self.theta),self.coordinates[1]+self.radius*math.sin(self.theta),
                         #  self.coordinates[0]+self.radius*(math.cos(self.theta)*10),self.coordinates[1]+self.radius*(math.sin(self.theta)*10),fill="black",arrow = tk.LAST,tags="que")"""
        
    def strike(self,ball,canvas,window):
        speed_x = (5*(math.cos(self.theta)))
        speed_y = (5*(math.sin(self.theta)))
        ball.move(canvas,(speed_x,speed_y),window)
        canvas.delete(self.que)
        print(ball.get_coordinates())
        self.coordinates =  ball.get_coordinates()
        x1 =(self.coordinates[0]+self.radius*math.cos(self.theta))-(ball_size/2)
        y1 = (self.coordinates[1]+self.radius*math.sin(self.theta))-(ball_size/2)
        x2 = (self.coordinates[0]+self.radius*(math.cos(self.theta)*10))+(ball_size/2)
        y2 = (self.coordinates[1]+self.radius*(math.sin(self.theta)*10))+(ball_size/2)
        self.que = canvas.create_line(x1,y1,x2,y2,fill="black",arrow = tk.LAST,tags="que")
        
        # self.que = canvas.create_line(self.coordinates[0]+self.radius*math.cos(self.theta),self.coordinates[1]+self.radius*math.sin(self.theta),
                           #self.coordinates[0]+self.radius*(math.cos(self.theta)*10),self.coordinates[1]+self.radius*(math.sin(self.theta)*10),fill="black",arrow = tk.LAST,tags="que")
    
    

        
        
        






        


    





def __main__():


    window = tk.Tk()
    window.title("8 Ball pool")

    canvas = tk.Canvas(window,bg="green",height = 400, width=800)
    canvas.pack()

    white_ball = Ball((200,200),"snow",canvas)
    for i in range (ball_amount):
        window.update()
        ball_lst.append(Ball((750,100-(ball_size+1)*i),colors[i],canvas))
    que = Que(white_ball.get_coordinates(),angle,canvas)

    def move_cursor(buttonpress):
        if buttonpress == "left":
            que.move_que(-1,canvas)
        elif buttonpress == "right":
            que.move_que(1,canvas)
        
    def move_after_strike(que):
        del que
        que = Que(white_ball.get_coordinates(),angle,canvas)
        return que




    



    window.update()
    window.bind("<Left>", lambda event: move_cursor("left"))
    window.bind("<Right>", lambda event: move_cursor("right"))
    window.bind("<Up>", lambda event: que.strike(white_ball,canvas,window))
    window.mainloop()

    
    



if __name__ == "__main__":
    __main__()



