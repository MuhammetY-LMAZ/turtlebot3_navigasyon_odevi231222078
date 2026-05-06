#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def hedefe_git(x, y, z, w):
    # Navigasyon sunucusuna bağlan
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Koordinatları ata
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    rospy.loginfo(f"Hedefe gidiliyor... X: {x}, Y: {y}")
    client.send_goal(goal)
    
    # Hedefe varana kadar bekle
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('robot_odev_node')

        # --- BURAYA KENDİ ALDIĞIN 5 KOORDİNATI YAZ ---
        # Format: (x, y, orientation_z, orientation_w)
        points = [
            (1.2, 0.5, 0.0, 1.0),   # 1. Nokta
            (2.0, -1.0, 0.0, 1.0),  # 2. Nokta
            (0.0, -2.5, 0.0, 1.0),  # 3. Nokta
            (-1.5, 0.0, 0.0, 1.0),  # 4. Nokta
            (0.5, 0.5, 0.0, 1.0)    # 5. Nokta
        ]

        for p in points:
            hedefe_git(p[0], p[1], p[2], p[3])
            rospy.loginfo("Hedefe ulasildi! 2 saniye bekleniyor...")
            rospy.sleep(2) # Noktalar arası bekleme (isteğe bağlı)

        rospy.loginfo("TÜM GÖREVLER TAMAMLANDI!")

    except rospy.ROSInterruptException:
        rospy.loginfo("Görev iptal edildi.")
