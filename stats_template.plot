# kAFL Status Plot
#
# Adopted from Redqueen kAFL-Fuzzer/common/evaluation.py
#
# Copyright 2019 Sergej Schumilo, Cornelius Aschermann
# Copyright 2020 Intel Corporation
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#

# Launch as:
# $ gnuplot -c $tools/stats.plot $perform_dir/stats_1.csv $perform_dir/stats_2.csv

__INDATA__

set terminal wxt size 900,800 enhanced persist
set multiplot

set grid xtics linetype 0 linecolor rgb '#d0d0d0'
set grid ytics linetype 0 linecolor rgb '#d0d0d0'
set border linecolor rgb '#50c0f0'
set tics textcolor rgb '#000000'
set key outside
set size 1, 0.30
set datafile separator ';'

# auto-scale y axis but avoid empty [0:0] yrange warning when no values yet
set yrange [0:*]

#set xlabel "Time"
set xdata time
set format x "%H:%M"
set timefmt "%s"
set style line 2
set style data line
set origin 0.0,0.66

## plot #1
plot __PLOT1__

## plot #2
set origin 0.0,0.33
plot __PLOT2__

## plot #3
set origin 0.0,0.0
plot __PLOT3__

unset multiplot
#pause 2
#reset
#reread
