import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import glob
import math
import matplotlib.ticker as mtick

if len(sys.argv)<2:
	print("Usage: python plot_reference_atlas_regions [nutil directory]")
	exit(1)


report_files = glob.glob(sys.argv[1]+"/**/*RefAtlasRegions.csv", recursive = True)
#report_files = glob.glob(sys.argv[1]+"/**/*RefAtlasRegions_*.csv", recursive = True)
atlas_files = glob.glob(sys.argv[1]+"/**/*.label", recursive = True)


color_map = {}

def load_labels(file):
	
	with open(file,'r') as f:
		line = f.readline()
		while line:
			line = f.readline().strip()
			if (not line.startswith("#")):
				line = line.replace("\"","").lower().split(",")[0]
				lst = line.split('\t')
				if len(lst)==8:
#					print(lst[7])
					color_map[lst[7]] = [float(lst[1])/256.0,float(lst[2])/256.0,float(lst[3])/256.0]

    

if len(report_files)==0:
	print("Could not find any reports to plot ")
	exit(1)

if len(atlas_files)==0:
	print("Could not find any atlas files ")
	exit(1)


load_labels(atlas_files[0])


#print(color_map)
#print(color_map["prepyramidal fissure"])


#print(report_files)

all_data = []
print("Loading...")
for r in report_files:
	df = pd.read_csv(r, sep=';')
	all_data.append(df)
#	print(r)
#print(df.head(1))



#print(df['Region area'])


# create map of data

dmap = {}
for df in all_data:
#	od = df['Region area']
	od = df['Load']

	for i in range(0,len(df)):
		key = df['Region Name'][i].lower().split(",")[0]
		#print(key)
		if (od[i]!=0):
			if (not key in dmap):
				dmap[key] = []

			dmap[key].append(od[i])



xx = 0
fig, ax = plt.subplots()
xticks = []
xp = []
fig.set_figwidth(10)
fig.set_figheight(5)
xp_colors = []
td = []
for key in dmap:

	d=[]
	x=[]
	sx = xx
	sz = 0
	for val in dmap[key]:
		d.append(val)
		td.append(val)
		x.append(xx)
		xx = xx + 1
		sz = sz + 1

#	print(len(dmap[key]))

	c = color_map[key]
	if sz>=0:
		xticks.append(key)
		xp.append(sx + (sz)/2.0)
		xp_colors.append((c[0],c[1],c[2]))



	p1 = ax.bar(x,d, width=2.0, color=(c[0],c[1],c[2]))
	#ax.bar_label(p1, label_type='center')
	ax.set_ylabel('Load')

ticks = plt.xticks(xp, xticks,rotation = 45, fontsize=6)


for label in ax.get_xmajorticklabels():
    label.set_horizontalalignment("right")

fmt = '%.2f%%' # Format you want the ticks, e.g. '40%'
yticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(yticks)

avg = sum(td)/len(td)
sigma = 0.0
for i in td:
	sigma = sigma + (avg-i)*(avg-i)/(len(td)-1)


sigma = math.sqrt(sigma)
#print(str(avg) + " ," +str(sigma))
#plt.ylim((avg+sigma*3),0)

#for ticklabel, tickcolor in zip(plt.gca().get_xticklabels(), xp_colors):
#   ticklabel.set_color(tickcolor)

ax.xaxis.set_ticks_position('bottom') 
[t.set_color(i) for (i,t) in
 zip(xp_colors,ax.xaxis.get_ticklabels())]

plt.tight_layout()
plt.savefig('ref_plot.png',dpi=180)
plt.show()
plt.draw()
