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
