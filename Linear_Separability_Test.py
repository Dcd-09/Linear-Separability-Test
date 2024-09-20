from scipy.spatial import ConvexHull
import numpy as np


def ls_test(x):
    """Determine if the point set (two categories) is linearly separable.

    Args:
        x (np.array): (N, M+1), point set, N is the number of points, M is the number of dimensions;
        The '1' in 'M+1' represents the label of the point, and the label is placed at the end, represented by 1 and -1.
    Example:
        x = np.array([[0, 1, 3, 1],
                      [3, 2, 4, -1]])
        In this example, 'x' contains two points, which are [0, 1, 3] and [3, 2, 4], 1 and -1 are their labels, respectively.
    Returns:
        '1' indicates that the set is linearly separable(LS);
        '-1' indicates that the set is non linearly separable(NLS).
    """
    set_a = []
    set_b = []
    for i in range(x.shape[0]):
        if x[i][-1] == 1:
            set_a.append(x[i][:-1].tolist())
        else:
            set_b.append(x[i][:-1].tolist())
    set_a = np.array(set_a)
    set_b = np.array(set_b)
    coor_origin = np.zeros([1, x.shape[1] - 1], dtype=x.dtype)
    set_gd = set_a[None, ...] - set_b[:, None, :]
    set_gd = set_gd.reshape(-1, x.shape[1]-1)
    hull = ConvexHull(set_gd)
    set_vertices = set_gd[hull.vertices]
    for i in set_vertices:
        if np.all(coor_origin[0] == i):
            return -1
    set_gd_origin = np.vstack((set_vertices, coor_origin))
    hull = ConvexHull(set_gd_origin)
    set_vertices = set_gd_origin[hull.vertices]
    for i in set_vertices:
        if np.all(coor_origin[0] == i):
            return 1
    return -1

