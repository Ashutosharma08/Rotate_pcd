import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud('concate.ply')
pcd.paint_uniform_color([1,0,0])
pcd1 = o3d.io.read_point_cloud('TSY 2/TSY_AC_AA/TreeFiles/1.ply')
pcd1.paint_uniform_color([0,1,1])
# downpcd = pcd.voxel_down_sample(voxel_size = 0.05)
# normal=downpcd.estimate_normals(
#     search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)) # normals facing upwards

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
vis.add_geometry(pcd1)
vis.run()
vis.destroy_window()