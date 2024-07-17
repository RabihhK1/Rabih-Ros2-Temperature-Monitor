import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertPublisher(Node):

    def __init__(self):
        super().__init__('alert_publisher')
        self.subscription = self.create_subscription(
            String,
            'alert_trigger',
            self.alert_callback,
            10)
        self.alert_publisher = self.create_publisher(String, 'alert', 10)

    def alert_callback(self, msg):
        alert_message = msg.data
        self.get_logger().info(f'Publishing alert: {alert_message}')
        alert_msg = String()
        alert_msg.data = alert_message
        self.alert_publisher.publish(alert_msg)

def main(args=None):
    rclpy.init(args=args)
    alert_publisher = AlertPublisher()
    rclpy.spin(alert_publisher)
    alert_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
