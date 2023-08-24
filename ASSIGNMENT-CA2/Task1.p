set title "Task1"
set xlabel "TCP Streams"
set ylabel "PDR (%)"

set xrange [0:100]
set yrange [0:100]

set grid

set boxwidth 10

set key top right

plot "/home/eryk/Desktop/gnu/Task1.tr" using 1:2 with line title "Packets Rx", "/home/eryk/Desktop/gnu/Task1.tr" using 2:2 with line title "Packets Tx" ;
replot

set term post eps enhan color 'Helvetica, 31'
set out "Task1.eps" ; replot
