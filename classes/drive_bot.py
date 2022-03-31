class DriveBot():
    all_disabled = False
    latitude = -999999
    longitude = -999999

    robot_count = 0

    def __init__(self, motor_speed = 0, sensor_range = 0, direction = 0) -> None:
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
    
    def __repr__(self) -> str:
        print('Robot with {} was created'.format(self.id))
    
    def control_bot(self, motor_speed, direction) -> None:
        self.motor_speed = motor_speed
        self.direction = direction
    
    def adjust_sensor(self, sensor_range) -> None:
        self.sensor_range = sensor_range
