EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:rfm70
LIBS:bluetooth
LIBS:DRILLS
LIBS:FLASH_MEMORY
LIBS:lm1117
LIBS:lm2596
LIBS:stm32
LIBS:transil
LIBS:tech-thing
LIBS:USB_CONNECTORS
LIBS:mcp73832
LIBS:nrf24l01
LIBS:tps61085
LIBS:sma
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 7 7
Title ""
Date "20 mar 2014"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L M25P010-AVMN6P U7
U 1 1 53288046
P 5700 3950
F 0 "U7" H 5700 4450 60  0000 C CNN
F 1 "M25P010-AVMN6P" H 5700 3700 60  0000 C CNN
F 2 "~" H 5700 3950 60  0000 C CNN
F 3 "~" H 5700 3950 60  0000 C CNN
	1    5700 3950
	1    0    0    -1  
$EndComp
$Comp
L C C31
U 1 1 53288055
P 5700 2850
F 0 "C31" H 5700 2950 40  0000 L CNN
F 1 "100nF" H 5706 2765 40  0000 L CNN
F 2 "~" H 5738 2700 30  0000 C CNN
F 3 "~" H 5700 2850 60  0000 C CNN
	1    5700 2850
	1    0    0    -1  
$EndComp
$Comp
L +3,3V #PWR090
U 1 1 53288079
P 6700 3500
F 0 "#PWR090" H 6700 3460 30  0001 C CNN
F 1 "+3,3V" H 6700 3610 30  0000 C CNN
F 2 "" H 6700 3500 60  0000 C CNN
F 3 "" H 6700 3500 60  0000 C CNN
	1    6700 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 3600 6700 3600
Wire Wire Line
	6700 3600 6700 3500
$Comp
L DGND #PWR091
U 1 1 53288082
P 4700 4150
F 0 "#PWR091" H 4700 4150 40  0001 C CNN
F 1 "DGND" H 4700 4080 40  0000 C CNN
F 2 "~" H 4700 4150 60  0000 C CNN
F 3 "~" H 4700 4150 60  0000 C CNN
	1    4700 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 4050 4700 4050
Wire Wire Line
	4700 4050 4700 4150
$Comp
L DGND #PWR092
U 1 1 5328809C
P 5700 3150
F 0 "#PWR092" H 5700 3150 40  0001 C CNN
F 1 "DGND" H 5700 3080 40  0000 C CNN
F 2 "~" H 5700 3150 60  0000 C CNN
F 3 "~" H 5700 3150 60  0000 C CNN
	1    5700 3150
	1    0    0    -1  
$EndComp
$Comp
L +3,3V #PWR093
U 1 1 532880C0
P 5700 2550
F 0 "#PWR093" H 5700 2510 30  0001 C CNN
F 1 "+3,3V" H 5700 2660 30  0000 C CNN
F 2 "" H 5700 2550 60  0000 C CNN
F 3 "" H 5700 2550 60  0000 C CNN
	1    5700 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	5700 2650 5700 2550
Wire Wire Line
	5700 3150 5700 3050
Text GLabel 4700 3600 0    39   Input ~ 0
FLASH_CS
Text GLabel 4700 3750 0    39   Input ~ 0
FLASH_MISO
Text GLabel 6700 3900 2    39   Input ~ 0
FLASH_CLK
Text GLabel 6700 4050 2    39   Input ~ 0
FLASH_MOSI
Text GLabel 4700 3900 0    39   Input ~ 0
FLASH_nWP
Text GLabel 6700 3750 2    39   Input ~ 0
FLASH_nHOLD
Wire Wire Line
	4700 3600 4800 3600
Wire Wire Line
	4700 3750 4800 3750
Wire Wire Line
	4700 3900 4800 3900
Wire Wire Line
	6700 3750 6600 3750
Wire Wire Line
	6600 3900 6700 3900
Wire Wire Line
	6600 4050 6700 4050
$EndSCHEMATC
