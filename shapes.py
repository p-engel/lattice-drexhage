import numpy as np


def sphere(r):
    '''
    Michelangelo carves standard sphere
    Parmaeter: r -- scalar, radius
    '''
    x = np.linspace(-r, r, 2*r+1)
    y = np.linspace(-r, r, 2*r+1) 
    z = np.linspace(-r, r, 2*r+1) 
    
    xgrid, ygrid, zgrid = np.meshgrid(x, y, z) 
    XYZ = np.column_stack((
        np.ravel(xgrid),
        np.ravel(ygrid),
        np.ravel(zgrid)
    ))
    
    cond = ((XYZ[:, 0]**2 + XYZ[:, 1]**2 + XYZ[:, 2]**2) <= r**2)
    ptsout = XYZ[cond]
    return ptsout


def cuboid(min, max, offset=(0, 0, 0)):
    """
    Michelangelo carves cuboid
    Parameters:
        min -- tup: (xmin, ymin, zmin)
        max -- tup: (xmax, ymax, zmax)
        offset -- tup: (xshift, yshift, zshift)
            displace cuboid anlong x, y, z axes
    """

    r0 = np.asarray(min)
    r = np.asarray(max)
    shift = np.asarray(offset)

    length = np.absolute(r - r0) + 1
    x = np.linspace(r0[0], r[0], length[0]) + shift[0]
    y = np.linspace(r0[1], r[1], length[1]) + shift[1]
    z = np.linspace(r0[2], r[2], length[2]) + shift[2]

    xgrid, ygrid, zgrid = np.meshgrid(x, y, z) 
    XYZ = np.column_stack((
        np.ravel(xgrid),
        np.ravel(ygrid),
        np.ravel(zgrid)
    ))

    ptsout = XYZ
    return ptsout


def sphereonslab(min, max, r=1, offset=(0, 0, -3)):
    """
    Michelangelo carves sphere on slab
    Parameters
        for sphere: r -- scalar, radius
        for slab: min -- tup: (xmin, ymin, zmin)
                  max -- tup: (xmax, ymax, zmax)
                  offset -- tup: (xshift, yshift, zshift)
                      displace cuboid anlong x, y, z axes
    """
    
    spherexyz = sphere(r)
    slabxyz = cuboid(min, max, offset)
    
    ptsout = np.vstack((spherexyz, slabxyz))
    return ptsout


# out = sphereonslab((-1, -1, 0), (1, 1, 1))
# print(out)
# plt.scatter(out[:, 0], out[:, 2])
# plt.title('sphere on cuboid on integer grid')
# plt.axis('equal')
# plt.show()
