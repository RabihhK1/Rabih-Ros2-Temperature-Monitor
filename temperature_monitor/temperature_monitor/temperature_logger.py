import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import os

class TemperatureLogger(Node):

    def __init__(self, log_file_path):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.temperature_callback,
            10)
        self.log_file_path = log_file_path
       
        os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
        self.log_file = open(self.log_file_path, 'a')

    def temperature_callback(self, msg):
        temperature = msg.data
        self.get_logger().info(f'Logging temperature: {temperature:.2f}')
        self.log_file.write(f'{temperature:.2f}\n')

    def destroy_node(self):
        self.log_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)

    # Define the log file path
    log_file_path = 'src/temperature_monitor/temperature_log.txt'  # Change this path as needed

    temperature_logger = TemperatureLogger(log_file_path)
    rclpy.spin(temperature_logger)
    temperature_logger.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
