import turtle
n =  input("Enter the bits : ")
d = turtle.Turtle()
d.forward(1000)
d.backward(1000)
d.setheading(90)
d.forward(500)
d.backward(1000)
d.forward(500)
h = 30
w = 20
s = 0
lst = [int (i) for i in n]
if lst[0] == 0:
    d.backward(h)
    s = 0
else:
    d.forward(h)
    s = 1
for i in lst:
    if i==0:
        if s==1:
            d.backward(2*h)
            s = 0
        d.setheading(0)
        d.forward(w)
        d.setheading(90)
    else:
        if s==0:
            d.forward(2*h)
            s =  1
        d.setheading(0)
        d.forward(w)
        d.setheading(90)

import turtle
n =  input("Enter the bits : ")
d = turtle.Turtle()
d.forward(1000)
d.backward(1000)
d.setheading(90)
d.forward(500)
d.backward(1000)
d.forward(500)
h = 30
w = 20
lst = [int (i) for i in n]
d.setheading(90)
d.forward(h)
s = 1
for i in lst:
    if i==1:
        if s==1:
            d.backward(2*h)
            s = 0
        else:
            d.forward(2*h)
            s=1
        d.setheading(0)
        d.forward(w)
        d.setheading(90)
    else:
        d.setheading(0)
        d.forward(w)
        d.setheading(90)

  # manchester
import turtle
n = input("Enter the bits : ")
d = turtle.Turtle()
d.forward(1000)
d.backward(1000)
d.setheading(90)
d.forward(500)
d.backward(1000)
d.forward(500)
h  =70
w = 30
d.forward(h)
d.setheading(0)
s = 1
for i in n:
    if i == "1":
        if s==1:
            d.forward(w)
            d.setheading(90)
            d.backward(2*h)
            d.setheading(0)
            d.forward(w)
            s=0
        else:
            d.setheading(90)
            d.forward(2*h)
            d.setheading(0)
            d.forward(w)
            d.setheading(90)
            d.backward(2*h)
            d.setheading(0)
            d.forward(w)
    else:
        if s == 0:
            d.forward(w)
            d.setheading(90)
            d.forward(2*h)
            d.setheading(0)
            d.forward(w)
            s= 1
        else:
            d.setheading(90)
            d.backward(2*h)
            d.setheading(0)
            d.forward(w)
            d.setheading(90)
            d.forward(2*h)
            d.setheading(0)
            d.forward(w)


# First simulation   

set ns [new Simulator]

# Two files to store our simulation results 

set tr [ open "out.tr" w]

$ns trace-all $tr

set ftr [open "out.nam" w]

$ns namtrace-all $ftr


# Creating Nodes 

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

$ns duplex-link $n0 $n1 10mb 10ms DropTail
$ns duplex-link $n1 $n2 10mb 10ms DropTail

set tcp1 [new Agent/TCP]
set sink [new Agent/TCPSink]

$ns queue-limit $n0 $n1 5
$ns queue-limit $n1 $n2 5
$ns attach-agent $n0 $tcp1
$ns attach-agent $n1 $sink

$ns connect $tcp1 $sink

proc finish { } {
      global ns tr ftr
      $ns flush-trace
      close $tr
      close $ftr
      exec nam out.nam &
      exit
}
set ftp [new Application/FTP]

$ftp attach-agent $tcp1

set tcp2 [new Agent/TCP]
set sink2 [new Agent/TCPSink]

$ns attach-agent $n1 $tcp2
$ns attach-agent $n2 $sink2
$ns connect $tcp2 $sink2

set ftp1 [new Application/FTP]

$ftp1 attach-agent $tcp2

$ns at .1 "$ftp start"

$ns at .2 "$ftp1 start" 

$ns at 4.0 "$ftp stop"

$ns at 4.0 "$ftp1 stop"

$ns at 2.1 "finish"

$ns run
