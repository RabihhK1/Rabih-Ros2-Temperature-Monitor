import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class ThresholdSubscriber(Node):

    def __init__(self):
        super().__init__('threshold_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.temperature_callback,
            10)
        self.alert_publisher = self.create_publisher(String, 'alert_trigger', 10)
        self.threshold = 30.0  # Example threshold value

    def temperature_callback(self, msg):
        temperature = msg.data
        if temperature > self.threshold:
            self.get_logger().info(f'Temperature {temperature:.2f} exceeds threshold {self.threshold}')
            alert_msg = String()
            alert_msg.data = f'Alert: Temperature {temperature:.2f} exceeds threshold {self.threshold}'
            self.alert_publisher.publish(alert_msg)

def main(args=None):
    rclpy.init(args=args)
    threshold_subscriber = ThresholdSubscriber()
    rclpy.spin(threshold_subscriber)
    threshold_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
