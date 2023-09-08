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
    TTLServo.xyInput((170), -110)
    
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


#loop
robot = Robot()

#ruedas
controller.buttons[6].observe(lambda change: avanzar(), names='value')
controller.buttons[4].observe(lambda change: izquierda(), names='value')
controller.buttons[5].observe(lambda change: derecha(), names='value')


#brazo
controller.buttons[12].observe(lambda change: subir(), names='value')
controller.buttons[13].observe(lambda change: bajar(), names='value')
controller.buttons[0].observe(lambda change: agarrar(), names='value')
controller.buttons[1].observe(lambda change: soltar(), names='value')

