import argparse
import matplotlib.pyplot as plt
import pandas as pd
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 14
})

parser = argparse.ArgumentParser(
    description='plot dda shape.dat on a plane')
parser.add_argument(
    'datfile',
    help='the dda shape.dat file',
)
parser.add_argument(
    '-x', '--xnormal',
    help='x normal to yz plane',
    action='store_const', const='xnormal', 
    dest='mode'
)
parser.add_argument(
    '-y', '--ynormal',
    help='y normal to xz plane',
    action='store_const', const='ynormal',
    dest='mode'
)
parser.add_argument(
    '-z', '--znormal',
    help='z normal to xy plane',
    action='store_const', const='znormal',
    dest='mode'
)
args = parser.parse_args()

# read file and skip 7 header-lines
filename = args.datfile
df = pd.read_csv(filename, sep='\t', header=None,
    usecols=[1, 2, 3, 4], index_col=0, skiprows=7,
    names= ['counts', 'x', 'y', 'z']
)

x = df['x'].to_numpy()
y = df['y'].to_numpy()
z = df['z'].to_numpy()

# graph
fig, ax = plt.subplots()

if args.mode == 'xnormal':
    alabel = 'y'; blabel = 'z';
    a = y; b = z;
elif args.mode == 'ynormal':
    alabel = 'x'; blabel = 'z';
    a = x; b = z;
elif args.mode == 'znormal':
    alabel = 'x'; blabel = 'y'
    a = x; b = y;
else:
    print('nothing here to see\
        use help option')
    sys.exit()

ax.scatter(a, b,
	linestyle='dashed', linewidth=3, color='tab:blue')
ax.set_xlabel(alabel)
ax.set_ylabel(blabel)
ax.set_title("shape file")
                                                       
plt.axis('equal')
plt.show(block=True)
