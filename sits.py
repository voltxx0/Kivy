from kivy.uix.label import Label
from kivy.clock import Clock




class Sits(Label):
   def __init__(self, total, **kwargs):
       self.current = 0
       self.total = total
       my_text = "Squats left: " + str(self.total)
       super().__init__(text=my_text, **kwargs)
