import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float32

class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.publish_temperature)

    def publish_temperature(self):
        temperature = random.uniform(20.0, 40.0)  # Simulated temperature
        msg = Float32()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing temperature: {temperature:.2f}')

def main(args=None):
    rclpy.init(args=args)
    temperature_publisher = TemperaturePublisher()
    rclpy.spin(temperature_publisher)
    temperature_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
