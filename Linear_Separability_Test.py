from scipy.spatial import ConvexHull
import numpy as np


def whetherLinearSeparable(x):
    set_a = []
    set_b = []
    for i in range(x.shape[0]):
        if x[i][-1] == 1:
            set_a.append(x[i][:-1].tolist())
        else:
            set_b.append(x[i][:-1].tolist())
    set_a = np.array(set_a)
    set_b = np.array(set_b)
    set_gd = set_a[None, ...] - set_b[:, None, :]
    set_gd = set_gd.reshape(-1, x.shape[1]-1)
    hull = ConvexHull(set_gd)
    first_idx = np.sort(hull.vertices)
    coor_origin = np.zeros([1, x.shape[1]-1], dtype=x.dtype)
    set_gd_origin = np.vstack((set_gd, coor_origin))
    hull = ConvexHull(set_gd_origin)
    second_idx = np.sort(hull.vertices)
    if len(first_idx) == len(second_idx):
        if np.all(first_idx == second_idx):
            return -1
        else:
            return 1
    else:
        return 1


if __name__ == '__main__':

    x = np.array([[-0.5,-0,-1],[3.5,4.1,-1],[4.5,6,1],[-2,-2.0,-1],[-4.1,-2.8,-1],[1,3,-1],[-7.1,-4.2,1],
                  [-6.1,-2.2,1],[-4.1, 2.2, 1],[1.4,4.3,1],[-2.4,4.0,1],[-8.4,-5,1]])
    print(whetherLinearSeparable(x))
