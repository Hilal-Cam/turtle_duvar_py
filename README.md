# Duvardan Kaçan Kaplumbağa (turtle_duvar_py)

Bu proje, ROS 2 ortamında TurtleSim simülasyonundaki kaplumbağanın duvar sınırlarına (min: 1.0, max: 10.0) ulaştığında yön değiştirerek alan içerisinde kalmasını sağlar[cite: 1].

## Özellikler
- `/turtle1/pose` konusundan anlık konum bilgisi dinlenir (Subscriber).
- `/turtle1/cmd_vel` konusuna hız ve yön komutları gönderilir (Publishe).
- Konum bilgisi her saniye terminale loglanır (`get_logger().info`).
- Hız ve duvar sınır değerleri ROS 2 parametresi olarak tanımlanmıştır.

## Kurulum ve Çalıştırma Adımları

### 1. Çalışma Alanını Derleme
```bash
cd ~/ros2_ws
colcon build --packages-select turtle_duvar_py
source install/setup.bash 
### 1. Çalışma Alanını Derleme
```
### 2. Simülasyonu Başlatma (1. Terminal)
```bash
ros2 run turtlesim turtlesim_node
```
### 3.Duvardan Kaçma Düğümünü Çalıştırma (2. Terminal)
```bash
ros2 run turtle_duvar_py wall_avoider
```
EKRAN GÖRÜNTÜSÜ
![Uploading ekran.png…]()

