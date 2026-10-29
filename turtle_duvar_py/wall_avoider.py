import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class WallAvoiderNode(Node):
    def __init__(self):
        super().__init__('wall_avoider_node')

        # Bonus: Hız ve sınır parametreleri
        self.declare_parameter('linear_speed', 2.0)
        self.declare_parameter('angular_speed', 1.5)
        self.declare_parameter('min_limit', 1.0)
        self.declare_parameter('max_limit', 10.0)

        # Yayıncı (Publisher)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Abone (Subscriber)
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        # Loglama Zamanlayıcısı (Saniyede 1 kez)
        self.current_pose = None
        self.timer = self.create_timer(1.0, self.log_timer_callback)

    # Duvar Kontrolü ve Hareket Fonksiyonu
    def pose_callback(self, msg: Pose):
        self.current_pose = msg
        
        linear_speed = self.get_parameter('linear_speed').value
        angular_speed = self.get_parameter('angular_speed').value
        min_limit = self.get_parameter('min_limit').value
        max_limit = self.get_parameter('max_limit').value

        cmd = Twist()

        # Duvar sınırına ulaştı mı? (x veya y sınırda mı?)
        if (msg.x < min_limit or msg.x > max_limit or 
            msg.y < min_limit or msg.y > max_limit):
            # Sınıra çarptığında kavis çizerek duvardan uzaklaşsın
            cmd.linear.x = 0.5   
            cmd.angular.z = angular_speed  
        else:
            # Güvenli alandaysa düz ilerlesin
            cmd.linear.x = linear_speed   
            cmd.angular.z = 0.0

        self.publisher_.publish(cmd)

    # Loglama Fonksiyonu
    def log_timer_callback(self):
        if self.current_pose is not None:
            self.get_logger().info(
                f'Konum -> X: {self.current_pose.x:.2f}, Y: {self.current_pose.y:.2f}'
            )

def main(args=None):
    rclpy.init(args=args)
    node = WallAvoiderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
