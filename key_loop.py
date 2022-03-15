import open3d as o3d
import keyboard
pcd = o3d.io.read_point_cloud('Normal1.ply')
vis = o3d.visualization.Visualizer()
vis.create_window(height=800,width=1200)
vis.add_geometry(pcd)
ctrl = vis.get_view_control()

for i in range(200000):
    ctrl.rotate(0,10)
    vis.poll_events()
    vis.update_renderer()
    if keyboard.is_pressed('q'):
        vis.destroy_window()
        break
