import pyttsx3
import kivy
from kivy.uix.floatlayout import FloatLayout
import os
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
class h(App):
    def build(self):
        self.lay=FloatLayout()
        self.t=Label(pos_hint={'center_x':0.5,'center_y':0.7},font_size=50,size_hint=(2,.1))
        self.t1=Label(pos_hint={'center_x':0.5,'center_y':0.8},font_size=50,size_hint=(2,.1),color=[0.41,.42,.74,1])
        self.btn=Button(pos_hint={'x':0.2,'center_y':.1},text='0',font_size="20sp",background_color=(1,1,1,1),size=(10,10),size_hint=(.1,.1))        
        self.btn.bind(on_press=self.buttonClicked)
        self.btn18=Button(pos_hint={'x':0.3,'center_y':.1},text='.',font_size="20sp",background_color=(1,1,1,1),size=(10,10),size_hint=(.1,.1))        
        self.btn18.bind(on_press=self.buttonClicked18)
        self.btn1=Button(pos_hint={'x':0.1,'center_y':.2},text='1',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn1.bind(on_press=self.buttonClicked1)
        self.btn2=Button(pos_hint={'x':.2,'center_y':.2},text='2',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn2.bind(on_press=self.buttonClicked2)
        self.btn3=Button(pos_hint={'x':.3,'center_y':.2},text='3',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn3.bind(on_press=self.buttonClicked3)
        self.btn4=Button(pos_hint={'x':.1,'center_y':.3},text='4',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn4.bind(on_press=self.buttonClicked4)
        self.btn5=Button(pos_hint={'x':.2,'center_y':.3},text='5',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn5.bind(on_press=self.buttonClicked5)
        self.btn6=Button(pos_hint={'x':.3,'center_y':.3},text='6',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn6.bind(on_press=self.buttonClicked6)
        self.btn7=Button(pos_hint={'x':.1,'center_y':.4},text='7',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn7.bind(on_press=self.buttonClicked7)
        self.btn8=Button(pos_hint={'x':.2,'center_y':.4},text='8',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn8.bind(on_press=self.buttonClicked8)
        self.btn9=Button(pos_hint={'x':.3,'center_y':.4},text='9',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn9.bind(on_press=self.buttonClicked9)
        self.btn10=Button(pos_hint={'x':.4,'center_y':.2},text='+',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn10.bind(on_press=self.buttonClicked10)
        self.btn11=Button(pos_hint={'x':.4,'center_y':.1},text='=',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn11.bind(on_press=self.buttonClicked11)
        self.btn12=Button(pos_hint={'x':.4,'center_y':.3},text='-',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn12.bind(on_press=self.buttonClicked12)
        self.btn13=Button(pos_hint={'x':.4,'center_y':.4},text='*',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn13.bind(on_press=self.buttonClicked13)
        self.btn14=Button(pos_hint={'x':.4,'center_y':.5},text='/',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn14.bind(on_press=self.buttonClicked14)
        self.btn15=Button(pos_hint={'x':.1,'center_y':.5},text='Clear',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn15.bind(on_press=self.buttonClicked15)
        self.btn16=Button(pos_hint={'x':.3,'center_y':.5},text='X',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn16.bind(on_press=self.buttonClicked16)
        self.btn17=Button(pos_hint={'x':.2,'center_y':.5},text='%',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn17.bind(on_press=self.buttonClicked17)
        self.btn19=Button(pos_hint={'x':.1,'center_y':.1},text='pow',font_size="20sp",background_color=(1,1,1,1),size=(25,30),size_hint=(.1,.1))
        self.btn19.bind(on_press=self.buttonClicked19)
        self.lay.add_widget(self.t)
        self.lay.add_widget(self.btn1)
        self.lay.add_widget(self.btn2)
        self.lay.add_widget(self.btn3)
        self.lay.add_widget(self.btn4)
        self.lay.add_widget(self.btn5)
        self.lay.add_widget(self.btn6)
        self.lay.add_widget(self.btn7)
        self.lay.add_widget(self.btn8)
        self.lay.add_widget(self.btn9)
        self.lay.add_widget(self.btn10)
        self.lay.add_widget(self.btn11)
        self.lay.add_widget(self.btn12)
        self.lay.add_widget(self.btn13)
        self.lay.add_widget(self.btn14)
        self.lay.add_widget(self.btn15)
        self.lay.add_widget(self.btn16)
        self.lay.add_widget(self.btn17)
        self.lay.add_widget(self.btn)
        self.lay.add_widget(self.btn18)
        self.lay.add_widget(self.t1)
        self.lay.add_widget(self.btn19)
        return self.lay
    def buttonClicked(self,btn):
        self.t.text=self.t.text+"0"
    def buttonClicked1(self,btn1):
        self.t.text=self.t.text+"1"
    def buttonClicked2(self,btn2):
        self.t.text=self.t.text+"2"
    def buttonClicked3(self,btn3):
        self.t.text=self.t.text+"3"
    def buttonClicked4(self,btn4):
        self.t.text=self.t.text+"4"
    def buttonClicked5(self,btn5):
        self.t.text=self.t.text+"5"
    def buttonClicked6(self,btn6):
        self.t.text=self.t.text+"6"
    def buttonClicked7(self,btn7):
        self.t.text=self.t.text+"7"
    def buttonClicked8(self,btn8):
        self.t.text=self.t.text+"8"
    def buttonClicked9(self,btn9):
        self.t.text=self.t.text+"9"
    def buttonClicked10(self,btn10):
        self.t.text=self.t.text+"+"
    def buttonClicked12(self,btn12):
        self.t.text=self.t.text+"-"
    def buttonClicked13(self,btn13):
        self.t.text=self.t.text+"*"
    def buttonClicked14(self,btn14):
        self.t.text=self.t.text+"/"
    def buttonClicked19(self,btn19):
        self.t.text=self.t.text+"**"    
    def buttonClicked15(self,btn14):
        self.t.text=''
        self.t1.text=''
    def buttonClicked17(self,btn14):
        self.t.text+='%'
    def buttonClicked18(self,btn18):
        self.t.text+='.'
    def buttonClicked16(self,btn14):
        k=str(self.t.text)
        self.t.text=k[:len(k)-1]
    def buttonClicked11(self,btn11):
        p=str(self.t.text)
        try:
            if(self.t.text==''):
                return True
            else:
               self.t1.text=str(eval(str(p)))
        except:
            self.t1.text="Error"    
if __name__=="__main__":
    h().run()
