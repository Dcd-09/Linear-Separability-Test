# Linear-Separability-Test
"Linear-Separability-Test.py" provides a function to determine whether a point set is linearly separable.

## Function Description
Given a set of points, the set can be divided into two subsets (A and B) based on the labels. According to paper 1, the linear separability of the two sets is equivalent to the linear separability of the _Minkowski difference_ set between the two sets and the Coordinate Origin.

Furthermore, to determine whether a point is linearly separable from a point set, we can consider whether the point is located within the convex hull of the set. If the point is within the convex hull, they are not linearly separable; if the point is outside the convex hull, they are linearly separable.

Finally, to determine the positional relationship between the point and the convex hull, a simple method is used here, which is to add the point to the point set composed of convex hull vertices and check whether the convex hull of this new point set has changed. If the convex hull remains unchanged, the point is within the convex hull; if the convex hull changes, the point is outside the convex hull.

This method is not the best, but because _scipy_ can help us calculate the convex hull, the program looks fairly simple.

## Reference
1. Zhong S, Lyu H, Lu X, Wang B, Wang D. A New Sufficient & Necessary Condition for Testing Linear Separability between Two Sets. IEEE Trans Pattern Anal Mach Intell. 2024 Jan 22;PP. doi: 10.1109/TPAMI.2024.3356661. Epub ahead of print. PMID: 38252586.
