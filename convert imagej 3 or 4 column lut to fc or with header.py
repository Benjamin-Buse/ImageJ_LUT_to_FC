import pandas as pd
import tkinter
import tkinter.filedialog
lutlocation = tkinter.filedialog.askopenfile(title="select imagej lut")
savelocation = tkinter.filedialog.asksaveasfilename(title="select save location")
df = pd.read_csv(lutlocation.name, sep="\s+", header=None)
if df.iat[0,0] == 'Index':
    df = pd.read_csv(lutlocation.name, sep="\s+")
f = open(savelocation,"a")
f.write(" False color description for MicroImage"+"\n")
f.write(" BEGIN Items"+"\n")
f.write(" Interpolate=0"+"\n")
for x in range(0,len(df)):
    if len(df.columns) == 3:
        r = df.iat[x,0]
        g = df.iat[x,1]
        b = df.iat[x,2]
    if len(df.columns) == 4:
        r = df.iat[x,1]
        g = df.iat[x,2]
        b = df.iat[x,3]
    rgbdecimal = b * 65536 + g * 256 +r
    f.write(" Item= "+str(x)+" "+str(x)+" "+str(rgbdecimal)+"\n")
f.write(" END Items")
f.close()