import open3d as o3d
import numpy as np
# np.set_printoptions(threshold=np.inf)
pcd = o3d.io.read_point_cloud('TSY 2/TSY_AC_AA/TreeFiles/1.ply')
downpcd = pcd.voxel_down_sample(voxel_size = 0.05)
normal=downpcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=20))  # normals facing upwards
print(pcd)
print(normal)
# print(normal.shape)
print(np.asarray(downpcd.normals))
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(downpcd)
vis.run()
vis.destroy_window()