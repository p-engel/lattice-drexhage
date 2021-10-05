import argparse
import shapes

parser = argparse.ArgumentParser(
    description='Create shape file with XYZ coordinates')
parser.add_argument(
    '-s', '--sphere',
    help='specify radius for standard shpere',
    nargs=1,
    type=int
)
parser.add_argument(
    '-c', '--cuboid',
    help='specify cartesian grid bounds as input \
        arguments: xmin, ymin, zmin, xmax, ymax, zmax',
    nargs='*',
    type=int
)
parser.add_argument(
    '-sc', '--sphereoncuboid',
    help='creates standard sphere on cuboid:\
        specify radius for sphere, the bounds of\
        the cartesian grid, and the offset of\
        the cuboid from the spere, all as input\
        args: xmin, ymin, zmin, xmax, ymax, zmax,\
            r, xshift, yshift, zshift',
    nargs='*',
    type=int
)
args = parser.parse_args()

if args.sphere:
    r = args.sphere[0]
    xyz = shapes.sphere(r)
elif args.cuboid:
    min = args.cuboid[0:3]
    max = args.cuboid[3:6]
    xyz = shapes.cuboid(min, max)
elif args.sphereoncuboid:
    min = args.sphereoncuboid[0:3]
    max = args.sphereoncuboid[3:6]

    if len(args.sphereoncuboid) == 6:
        xyz = shapes.sphereonslab(min, max)
    elif len(args.sphereoncuboid) == 7:
        r = args.sphereoncuboid[6]
        xyz = shapes.sphereonslab(min, max, r)
    else:
        r = args.sphereoncuboid[6]
        offset = args.sphereoncuboid[7:10]

        xyz = shapes.sphereonslab(min, max, r, offset)

else:
    print('nothing here to see\
        use help option')


# write shape file as dda dat file
file = open(str('shape.dat'), 'w')
file.write(str('Shape') + '\n')
file.write('\t' + str(len(xyz[:, 0])) +
    str(' = number of dipoles in target') + '\n')
file.write(str('1.000000 0.000000 0.000000 = A_1 vector') + '\n')
file.write(str('0.000000 1.000000 0.000000 = A_2 vector') + '\n')
file.write(str('1.000000 1.000000 1.000000 = (d_x,d_y,d_z)/d') + '\n')
file.write(str('0.000000 0.000000 0.000000 = (x,y,z)/d') + '\n')
file.write(str('JA  IX  IY  IZ ICOMP(x,y,z)') + '\n')
count = 0
for j in range(0, len(xyz[:, 0])):
    count = count + 1
    x = xyz[j, 0]
    y = xyz[j, 1]
    z = xyz[j, 2]
    file.write('\t' + str(count) + '\t' +
        str(int(x)) + '\t' + str(int(y)) + '\t' + str(int(z)) + '\t' +
        str(1) + '\t' + str(1) + '\t' + str(1) + '\n')
file.close()
