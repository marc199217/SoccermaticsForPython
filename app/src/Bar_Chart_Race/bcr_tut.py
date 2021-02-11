import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import bar_chart_race as bcr
import pandas as pd
import openpyxl

df = pd.read_excel("FML-Top20.xlsx")
df = df.fillna(0)
df = df.set_index("Season")
df = df.sort_index(ascending=True)

#Own figure settings 
plt.style.use(['dark_background', 'presentation.mplstyle'])
fig, ax = plt.subplots(figsize=(13.653, 7.68), dpi=300)
ax.set_xlim(900)
ax.invert_xaxis()
ax.set_title("Football Money League, from 2008/09 to 2019/20", fontsize=20)
#colors = {
#    "Deloitte Green": "#86BC25",
#    "Green 2": "#C4D600", 
#    "Green 4": "#43A72A",
#    "Accessible Green": "#26890D",
#    "Green 6": "#046A38",
#    "Accessible Teal": "#0D8390",
#    "Accessbible Blue": "#007CB0",
#    "Blue 5": "#005587",
#    "Blue 6": "#012169", 
#    "Teal 4": "#00ABAB",
#    "Teal 7": "#004F59",
#    "Cool Gray 4": "#BBBCBC",
#    "Cool Gray 6": "#A7A8AA",
#    "Cool Gray 9": "#75787B",
#    "Orange": "#ED8B00",
#    "Yellow": "#FFCD00",
#}

colors = ["#86BC25", "#C4D600", "#43A72A", "#26890D","#046A38","#0D8390","#007CB0","#005587","#012169","#00ABAB","#004F59","#BBBCBC","#A7A8AA","#75787B","#ED8B00","#FFCD00"]
cmap = ListedColormap(colors, name='mycmap')

#BCR settings
bcr.bar_chart_race(df, "FML-Top10_V3.mp4", 
                   fig=fig,
                   cmap=cmap,
                   filter_column_colors=True,
                   steps_per_period=50,
                   period_length=3000,
                   period_label={'x': .99, 'y': .5, 'ha': 'right', 'fontsize': 20},
                   n_bars=10,
                   bar_label_size=10,
                   bar_size=1, 
                   bar_kwargs={'alpha': 1, 'ec': 'white', 'lw': 1},
                   label_bars=True,
                   fixed_max=True)