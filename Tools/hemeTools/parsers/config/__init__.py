"""Regarding indices, a few conventions:

1) Broadly there are two types of index:

 - Three-dimensional indices into a 3D array, these are typically a
   numpy.ndarray (with shape == (3,)) and are named with a suffix of
   'Idx'.

 - One-dimensional indices into a flattened array. These are just
   integers and have the suffix 'Ijk'.

2) Indices can refer to a number of things and have additional naming:

 -  b : Index of a block

 - sg : Index of a site in the whole domain (site global)

 - sl : Index of a site in the block (site local)
 
"""