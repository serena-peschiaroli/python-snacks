import DriveBot
from OOP.drivebot import DriveBot

robot_1 = DriveBot.DriveBot(5, 10, 90)



print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)
robot_2 = DriveBot.DriveBot(35, 75, 25)
robot_3 = DriveBot.DriveBot(20, 60, 10)

DriveBot.DriveBot.longitude = -79.98553
DriveBot.DriveBot.latitude = 40.60793
DriveBot.DriveBot.all_disabled = False

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)