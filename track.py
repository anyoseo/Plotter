import Tkinter as tk
from chiplotle import *
plotter = instantiate_plotters()[0]

class Plotter(tk.Tk):

#Initialisation
    def __init__(self):
	plotter.select_pen(1)
	plotter.select_pen(0)
        tk.Tk.__init__(self)
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self, width=700, height=400,bg="white",cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.button_print = tk.Button(self, text = "START DRAWING", command = self.start_drawing)
        self.button_print.pack(side="top", fill="both", expand=True)
        self.button_clear = tk.Button(self, text = "CLEAR", command = self.clear_all)
        self.button_clear.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)
	self.resizable(width=False, height=False)

#Clear the drawing
    def clear_all(self):
        self.canvas.delete("all")
	del self.points_recorded[:]
	
#Start to printing
    def start_drawing(self):

	print("COORDONNEE")
	print(len(self.points_recorded))
	for r in self.points_recorded:
		print(r[0],r[1])
	plotter.write(hpgl.PD(self.points_recorded))
	plotter.select_pen(1)
	plotter.select_pen(0)

#Current Position
    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

#Draw on the window
    def draw_from_where_you_are(self, event):

        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y, 
                                self.x, self.y,fill="black")
	tuplePrevious=(self.previous_x,self.previous_y)	#Creation du tuple x,y precedent pour l'imprimante
	tupleXY=(self.x,self.y) #Creation du tuple x,y courant pour l'imprimante

	self.points_recorded.append((self.previous_x*20,11040-self.previous_y*20))
	self.points_recorded.append((self.x*20,11040-self.y*20)) #Ajuster les valeurs pour l'imprimante
	print(len(self.points_recorded))
	for val in self.points_recorded:
		print(val[0],val[1])
    
        self.previous_x = self.x
        self.previous_y = self.y

#Main
if __name__ == "__main__":
    app = Plotter()
    app.mainloop()
