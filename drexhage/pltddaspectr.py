import matplotlib
import matplotlib.pyplot as plt
import sys

import pandas as pd

matplotlib.rcParams.update({'font.size': 14})
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})


def pltspectr(filepath):
	"""
	plot dda spectrum file
	"""
	colnames = ['aeff', 'wave[um]', 'Qext',
                  'Qabs', 'Qsca'
    ]
	df = pd.read_csv(filepath, delim_whitespace=True,
           names=colnames, usecols=colnames
	)
	dfsort = df.sort_values(by=['wave[um]'])

	# plot
	x = 1.24 / dfsort['wave[um]']  # [eV]
	y = dfsort['Qsca']
	y1 = dfsort['Qabs']
	y2 = dfsort['Qext']

	fig, ax = plt.subplots()  # figure with a single axis.
	ax.plot(x, y,
		linestyle='dashed', linewidth=3,
		color='tab:blue', label='scattering')
	ax.plot(x, y2,
		linestyle='dashed', linewidth=3,
		color='tab:red', label='extinction')
	ax.plot(x, y1,
		linestyle='dashed', linewidth=3,
		color='tab:orange', label='absorption')
	ax.set_xlabel('eV')
	ax.set_ylabel('Q')
	ax.set_title("dda")
	ax.legend(loc='upper left', fontsize='small',
		frameon=False)

	plt.show(block=True)
	return


# plot Q factor of spectrum file
filepath = sys.argv[1]
pltspectr(filepath)
