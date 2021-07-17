""" Scope of a variable inherited to all sub-class instances because it's in the superclass
or just being in the subclass and not inheriting by other sub instances of the superclass """
class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    motor_speed = 0
    steps_per_minute = 0
    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False
class DriveBot(Robot):
  def __init__(self):
    pass
class WalkBot(Robot):
    step_length = 5
    pass
  
# Create the DriveBot class here!
drive_bot_1 = DriveBot()
drive_bot_1.motor_speed = 5
walk_bot_1 = WalkBot()
walk_bot_1.step_length = 5
walk_bot_1.steps_per_minute = 6
# Create the WalkBot class here!

# Uncomment the robot instantiation!
#robot_1 = DriveBot()
#robot_2 = WalkBot()
#robot_3 = WalkBot(20, 90, 15, 10)

# Use these print statements to test your code!


print(walk_bot_1.step_length)
print(drive_bot_1.steps_per_minute)
# Not supposed to be a variable of drive bot
# So use instance variable under walk bot class
print(drive_bot_1.motor_speed)



