EESchema Schematic File Version 4
LIBS:nas-mod-pi-cache
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J1
U 1 1 5DF92636
P 2800 1875
F 0 "J1" H 2850 2292 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 2850 2201 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Vertical_SMD" H 2800 1875 50  0001 C CNN
F 3 "~" H 2800 1875 50  0001 C CNN
	1    2800 1875
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J2
U 1 1 5DF93079
P 2800 2775
F 0 "J2" H 2850 3192 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 2850 3101 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Vertical_SMD" H 2800 2775 50  0001 C CNN
F 3 "~" H 2800 2775 50  0001 C CNN
	1    2800 2775
	1    0    0    -1  
$EndComp
Text Label 2600 2575 2    50   ~ 0
SW4
Text Label 2600 2675 2    50   ~ 0
SW5
Text Label 2600 2775 2    50   ~ 0
SW3
Text Label 2600 2875 2    50   ~ 0
SW2
Text Label 2600 2975 2    50   ~ 0
NC
Text Label 3100 2575 0    50   ~ 0
SW1a
Text Label 3100 2675 0    50   ~ 0
SW1b
Text Label 3100 2775 0    50   ~ 0
LED1
Text Label 3100 2875 0    50   ~ 0
LED2
Text Label 3100 2975 0    50   ~ 0
GND
Text Label 3100 3450 0    50   ~ 0
5V
Text Label 3100 3650 0    50   ~ 0
GND
Text Label 3100 4350 0    50   ~ 0
GND
Text Label 3100 4050 0    50   ~ 0
GND
Text Label 3100 1975 0    50   ~ 0
GND
Text Label 2600 1975 2    50   ~ 0
GND
Text Label 3100 1675 0    50   ~ 0
D3
Text Label 3100 1775 0    50   ~ 0
D1
Text Label 2600 1675 2    50   ~ 0
D2
Text Label 2600 1775 2    50   ~ 0
D0
Text Label 3100 2075 0    50   ~ 0
5V
Text Label 2600 2075 2    50   ~ 0
IREF
Text Label 3100 1875 0    50   ~ 0
EN
Text Label 2600 1875 2    50   ~ 0
RST
Text Label 2600 4050 2    50   ~ 0
EN
Text Label 2600 4150 2    50   ~ 0
RST
Text Label 2600 4550 2    50   ~ 0
SW1a
Text Label 2400 4650 2    50   ~ 0
SW1b
Text Label 2600 5150 2    50   ~ 0
SW2
Text Label 2600 4950 2    50   ~ 0
SW3
Text Label 2600 4450 2    50   ~ 0
SW4
Text Label 2600 4750 2    50   ~ 0
SW5
Text Label 2600 4850 2    50   ~ 0
LED1
Text Label 2600 5050 2    50   ~ 0
LED2
Text Label 2600 3550 2    50   ~ 0
D3
Text Label 2600 3650 2    50   ~ 0
D2
Text Label 2600 3750 2    50   ~ 0
D1
Text Label 2600 3950 2    50   ~ 0
D0
$Comp
L Connector_Generic:Conn_02x20_Odd_Even J3
U 1 1 5DF95190
P 2800 4350
F 0 "J3" H 2850 5464 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 2850 5373 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 2800 4350 50  0001 C CNN
F 3 "~" H 2800 4350 50  0001 C CNN
	1    2800 4350
	1    0    0    -1  
$EndComp
Text Label 2600 3450 2    50   ~ 0
3V3
Text Label 2600 3850 2    50   ~ 0
GND
Text Label 2600 4650 2    50   ~ 0
GND
Text Label 2600 5350 2    50   ~ 0
GND
Text Label 2600 4250 2    50   ~ 0
3V3
Text Label 3100 3550 0    50   ~ 0
5V
Text Label 3100 4850 0    50   ~ 0
GND
Text Label 3100 5050 0    50   ~ 0
GND
Wire Wire Line
	2400 4650 2600 4650
Text Label 2400 2075 2    50   ~ 0
GND
Wire Wire Line
	2400 2075 2600 2075
$EndSCHEMATC
