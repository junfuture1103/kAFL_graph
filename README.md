# kAFL_graph
this is kAFL Performance measurement tool

## Usage
after you git clone this repository, you have to bring your .csv file
### 1. Install Gnuplot
```
   sudo apt install gnuplot
```
### 2. Use Auto generation tool
If you want to compare multiple fuzzing results, use the -num option.
```
python3 autoplot.py (-num N)
```
### 3. Just Do It
```
gnuplot -c [.plot code] [csv file]
```
If you use -num option
```
gnuplot -c [.plot code] [csv file1] [csv file2] ... [csv fileN]
```

### if you want to see Other indicators, follow this description
you can edit autoplot.py yourself
```
#in autoplot.py

...

for i in range (1, int(args.num)+1):
        indata += 'indata'+str(i)+' = ARG'+str(i)+'\n'
        #PLOT1 - Total execs
        plot1_data += 'indata' + str(i) + ' using '
        plot1_data += '1:12' #data        
        plot1_data += ' title '
        plot1_data += '\'Total execs ' + str(i) + '\' ' #Title
        plot1_data += 'with line linecolor rgb '
        plot1_data += '\'#0090ff\' ' #color
        plot1_data += 'linewidth 4, \\\n' #linewidth
...

```
you can check other indicator's number here

                1 cur_time-self.start_time,         # elapsed time
                2 cur_execs,                        # execs/sec
                3 self.data["paths_total"],         # paths total
                4 self.data["paths_pending"],       # paths pending
                5 self.data["favs_total"],          # favs total
                6 self.data["findings"]["crash"],   # unique crashes
                7 self.data["findings"]["kasan"],   # unique kasan
                8 self.data["findings"]["timeout"], # unique timeout
                9 self.data["max_level"],           # max level
                10 self.data["cycles"],             # cycles
                11 self.data["favs_pending"],       # favs pending
                12 self.data["total_execs"],        # current total execs
                13 self.data["bytes_in_bitmap"],    # unique edges % p(col)
                
![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/794bcbd7-60aa-4947-9abd-538f377178c4/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/794bcbd7-60aa-4947-9abd-538f377178c4/Untitled.png)
