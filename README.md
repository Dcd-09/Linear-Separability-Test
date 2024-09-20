# Linear-Separability-Test
"Linear-Separability-Test.py" provides a function to determine whether a point set is linearly separable.

## Process Description
Given a set of points, the set can be divided into two subsets (A and B) based on the labels. According to paper 1, the linear separability of the two sets is equivalent to the linear separability of the **Minkowski difference** set between the two sets and the Coordinate Origin.

Furthermore, to determine whether a point is linearly separable from a point set, we can consider whether the point is located within the convex hull of the set. If the point is within the convex hull, they are not linearly separable; if the point is outside the convex hull, they are linearly separable.

Finally, to determine the positional relationship between _the point_ and the convex hull (referred to as the "original convex hull"), a simple method is used here, which is to add _the point_ to the point set composed of the vertices of the original convex hull and check whether the convex hull of the new point set has changed (Before that, it is necessary to determine whether _the point_ is the vertex of the original convex hull). If the new convex hull is consistent with the original convex hull, then _the point_ is located within the original convex hull; If the new convex hull changes (_the point_ becomes a new vertex), _the point_ is located outside the original convex hull.

This method is not the best, but because **scipy** can help us calculate the convex hull, the program looks relatively simple.

## Reference
1. Zhong S, Lyu H, Lu X, Wang B, Wang D. A New Sufficient & Necessary Condition for Testing Linear Separability between Two Sets. IEEE Trans Pattern Anal Mach Intell. 2024 Jan 22;PP. doi: 10.1109/TPAMI.2024.3356661. Epub ahead of print. PMID: 38252586.
