import open3d as o3d
import numpy as np
import os
import keyboard



forest_name = 'TSY 2/'
format_file = '.ply'
directory = os.path.join(forest_name)
treeFolderName = '/TreeFiles/'
for dirname in os.walk(directory):
    folders = dirname
    break

folder = folders[1][0]
folder_path = os.path.join(forest_name + folder + '/')
treeFolder = folder_path + treeFolderName

dummyNames = []
for filenames in os.walk(treeFolder):
    # files += len(filenames[2])
    dummyNames = filenames[2]
    break

ply_data = []
for treeFile in dummyNames:
    if treeFile.endswith(format_file):
        ply_data.append(treeFile)

# print(ply_data)
circle = 'circle'
lst3 = [s for s in ply_data if circle not in s]
print(lst3)




def create_normal_files(ply_data):

    # np.set_printoptions(threshold=np.inf)
    ply_path = 'TSY 2/TSY_AC_AA/TreeFiles/'
    ply_file = ply_path + ply_data
    pcd = o3d.io.read_point_cloud(ply_file)
    down = pcd.voxel_down_sample(voxel_size = 0.05)

    normal=down.estimate_normals(
        search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)) #normals random facing
    n = np.asarray(down.normals)
    b = np.asarray(down.points)


    #combining both points and normal so that we can access those points who have normal == 1
    concate = np.concatenate((b,n),axis=1)
    # print(concate.shape)
    lst = []
    for i in range(len(concate)):
        if concate[i][5] == 1:
            lst.append(concate[i][:3])
    # print(type(lst))
    arr = np.asarray(lst)
    # print(len(arr))
    filename = 'Normal'+ply_data

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(arr)
    o3d.io.write_point_cloud(filename, pcd)


# for i in lst3:
#     create_normal_files(i)
# print("Normal file ready, Sir!")

normal_file = []
for i in os.listdir():
    if i.endswith(format_file):
        normal_file.append(i)
# print(normal_file)
vis = o3d.visualization.Visualizer()
vis.create_window()
for i in range(len(lst3)):

    tree_file_path = 'TSY 2/TSY_AC_AA/TreeFiles/'+lst3[i]
    pcd = o3d.io.read_point_cloud(tree_file_path)
    pcd.paint_uniform_color([0,0,1])
    pcd1 = o3d.io.read_point_cloud(normal_file[i])
    pcd1.paint_uniform_color([1,0,0])

    vis.add_geometry(pcd)
    vis.add_geometry(pcd1)
    ctrl = vis.get_view_control()
    ctrl.rotate(0,-500)
    # vis.update_geometry(pcd)
    # vis.update_geometry(pcd1)
    print("first loop")
    for i in range(500000):
        ctrl.rotate(20,0)
        vis.poll_events()
        vis.update_renderer()
        if keyboard.is_pressed('1'):
            vis.remove_geometry(pcd)
            vis.remove_geometry(pcd1)
            break
            vis.update_geometry(pcd)
            vis.update_geometry(pcd1)
            vis.poll_events()
            vis.update_renderer()


# ply=o3d.io.read_point_cloud('Normal.ply')
# o3d.visualization.draw_geometries([ply])