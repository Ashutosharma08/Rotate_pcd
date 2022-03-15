import open3d as o3d
import numpy as np
# val = 1
np.set_printoptions(threshold=np.inf)
pcd = o3d.io.read_point_cloud('TSY 2/TSY_AC_AA/TreeFiles/1.ply')
down = pcd.voxel_down_sample(voxel_size = 0.05)
# normal = down.estimate_normals
normal=down.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)) #normals random facing
n = np.asarray(down.normals)
b = np.asarray(down.points)
# print(n)
print("---------------------------------")
# print(len(b))
#combining both points and normal so that we can access those points who have normal == 1
concate = np.concatenate((b,n),axis=1)
print(concate.shape)
lst = []
# lst2 = []
# print(n[0][2])
# print(len(n))
# print(n.size)
# vis = o3d.visualization.Visualizer()
# vis.create_window()
# vis.add_geometry(down)
# vis.run()
# vis.destroy_window()
for i in range(len(concate)):
    if concate[i][5] == 1:
        lst.append(concate[i][:3])
print(type(lst))
arr = np.asarray(lst)
print(len(arr))
filename = 'dem_con.ply'
# for i in range(len(n)):
#     if n[i][2] == -1:
#         lst2.append(n[i])
# print(lst2)

#converting list to numpy array:

# arr = np.asarray(lst)
# arr2 = np.asarray(lst2)

# print(arr.shape)
# print(arr2.shape)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(arr)
o3d.io.write_point_cloud(filename, pcd)

ply=o3d.io.read_point_cloud(filename)
o3d.visualization.draw_geometries([ply])