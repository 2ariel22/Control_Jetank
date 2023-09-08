# importando librerias
import ipywidgets.widgets as widgets
from jetbot import Robot
import traitlets
from SCSCtrl import TTLServo
import time as tm

#sincronizando el mando
controller = widgets.Controller(index=0)  # replace with index of your controller
display(controller)

#funciones Brazo
def bajar():
    TTLServo.xyInput(170, -110)
    
def subir():
    TTLServo.servoAngleCtrl(3, 10, 1, 150)
    tm.sleep(.5)
    TTLServo.servoAngleCtrl(2, 20, 1, 150)
    
def agarrar():
    TTLServo.servoAngleCtrl(4, -34, 1, 150)#cerrar griper
    tm.sleep(.5)

def soltar():
    TTLServo.servoAngleCtrl(4, 0, 1, 150)#cerrar griper
    tm.sleep(.5)

# funciones motor
def avanzar(change):
    if change['new'] == 1:
        robot.left(0.5)
        robot.right(0.5)
    else:
        robot.stop()

def izquierda(change):
    if change['new'] == 1:
        robot.left(0.3)
        robot.right(-0.3)
    else:
        robot.stop()

def derecha(change):
    if change['new'] == 1:
        robot.left(-0.3)
        robot.right(0.3)
    else:
        robot.stop()



def mover(change):
    x_speed = change['new'][0]
    y_speed = change['new'][1]
    if(y_speed >= 0.3):
        avanzar()
    elif(x_speed >= 0.3):
        derecha()
    elif(x_speed <= -0.3):
        izquierda()
    
def brazo(change):
    x_speed = change['new'][0]
    y_speed = change['new'][1]
    z_speed = change['new'][2]
    
#loop
robot = Robot()
    
controller.axes[0].observe(mover, names='value')
controller.axes[1].observe(brazo, names='value')

controller.buttons[12].observe(lambda change: subir(), names='value')
controller.buttons[13].observe(lambda change: bajar(), names='value')
 
controller.buttons[0].observe(lambda change: agarrar(), names='value')
controller.buttons[1].observe(lambda change: soltar(), names='value')

robot.stop()
