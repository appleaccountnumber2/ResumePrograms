""" Creating a robot changing moving direction . Just so one may see how I am organized and narrative"""
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    # Add the methods here!

    def control_bot(self,new_speed,new_direction):
""" changes the self.variable to a new value and overwrites it """
      self.motor_speed = new_speed
      self.direction = new_direction
    def adjust_sensor(self,new_sensor_range):
""" Overwrites self.sensor value with its parameter """
      self.sensor_range = new_sensor_range
robot_1 = DriveBot()
# Use the methods here!
# 90 degrees North
robot_1.sensor_range = 0
robot_1.motor_speed = 0
robot_1.direction = '90' + 'degrees'
robot_1.adjust_sensor(20)
robot_1.control_bot('10' + 'mph','270' + 'degrees')

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)