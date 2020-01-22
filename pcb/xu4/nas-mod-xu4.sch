EESchema Schematic File Version 4
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
Text Label 2600 3525 2    50   ~ 0
5V
Text Label 3100 3525 0    50   ~ 0
GND
Text Label 3100 1975 0    50   ~ 0
GND
Text Label 2600 1975 2    50   ~ 0
GND
Text Label 3100 1675 0    50   ~ 0
D7
Text Label 3100 1775 0    50   ~ 0
D5
Text Label 2600 1675 2    50   ~ 0
D6
Text Label 2600 1775 2    50   ~ 0
D4
Text Label 3100 2075 0    50   ~ 0
5V
Text Label 2600 2075 2    50   ~ 0
IREF
Text Label 3100 1875 0    50   ~ 0
EN
Text Label 2600 1875 2    50   ~ 0
RST
Text Label 3100 4225 0    50   ~ 0
EN
Text Label 3100 4125 0    50   ~ 0
RST
Text Label 2600 3725 2    50   ~ 0
SW1a
Text Label 2775 5125 2    50   ~ 0
SW1b
Text Label 3100 4725 0    50   ~ 0
SW2
Text Label 3100 4425 0    50   ~ 0
SW4
Text Label 3100 4525 0    50   ~ 0
SW5
Text Label 3100 4325 0    50   ~ 0
LED1-SGNL
Text Label 2600 4725 2    50   ~ 0
LED2
Text Label 3100 3725 0    50   ~ 0
D6
Text Label 3100 3825 0    50   ~ 0
D5
Text Label 3100 3925 0    50   ~ 0
D4
Text Label 2925 5125 0    50   ~ 0
GND
Text Label 2600 4925 2    50   ~ 0
1V8
Text Label 3100 4825 0    50   ~ 0
GND
Text Label 3100 4925 0    50   ~ 0
GND
Text Label 2400 2075 2    50   ~ 0
GND
Wire Wire Line
	2400 2075 2600 2075
Wire Wire Line
	2775 5125 2925 5125
Text Label 3100 4625 0    50   ~ 0
SW3
Text Label 3100 3625 0    50   ~ 0
D7
Text Label 4150 4275 2    50   ~ 0
LED1-SGNL
Text Label 5450 4800 0    50   ~ 0
GND
Wire Wire Line
	4700 4475 4700 4800
Wire Wire Line
	4700 4800 5450 4800
Text Label 5450 3675 0    50   ~ 0
5V
Wire Wire Line
	4700 4075 4700 4050
Wire Wire Line
	4700 4050 4975 4050
Wire Wire Line
	5275 3850 5275 3675
Wire Wire Line
	5275 3675 5450 3675
$Comp
L Device:R R2
U 1 1 5E262BDF
P 4700 3850
F 0 "R2" H 4770 3896 50  0000 L CNN
F 1 "10K" H 4770 3805 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4630 3850 50  0001 C CNN
F 3 "~" H 4700 3850 50  0001 C CNN
	1    4700 3850
	1    0    0    -1  
$EndComp
Connection ~ 4700 4050
Wire Wire Line
	4700 4000 4700 4050
Wire Wire Line
	5275 3675 4700 3675
Wire Wire Line
	4700 3675 4700 3700
Connection ~ 5275 3675
Text Label 5450 4675 0    50   ~ 0
LED1
Wire Wire Line
	5275 4675 5450 4675
$Comp
L Connector_Generic:Conn_02x15_Odd_Even J3
U 1 1 5DF95190
P 2800 4225
F 0 "J3" H 2850 5142 50  0000 C CNN
F 1 "Conn_02x15_Odd_Even" H 2850 5051 50  0000 C CNN
F 2 "Connector_PinSocket_2.00mm:PinSocket_2x15_P2.00mm_Vertical" H 2800 4225 50  0001 C CNN
F 3 "~" H 2800 4225 50  0001 C CNN
	1    2800 4225
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:BSS138 Q2
U 1 1 5E28545A
P 5175 4050
F 0 "Q2" H 5381 4096 50  0000 L CNN
F 1 "BSS138" H 5381 4005 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 5375 3975 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/BS/BSS138.pdf" H 5175 4050 50  0001 L CNN
	1    5175 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 4025 3300 4025
Wire Wire Line
	2400 3625 2600 3625
Wire Wire Line
	2400 4625 2600 4625
Wire Wire Line
	5275 4250 5275 4675
$Comp
L Transistor_FET:BSS138 Q1
U 1 1 5E1860F1
P 4600 4275
F 0 "Q1" H 4806 4321 50  0000 L CNN
F 1 "BSS138" H 4806 4230 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 4800 4200 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/BS/BSS138.pdf" H 4600 4275 50  0001 L CNN
	1    4600 4275
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 4275 4375 4275
Wire Wire Line
	4375 4275 4400 4275
Connection ~ 4375 4275
Wire Wire Line
	4375 4275 4375 4150
$Comp
L Device:R R1
U 1 1 5E24EF81
P 4375 4000
F 0 "R1" H 4445 4046 50  0000 L CNN
F 1 "10K" H 4445 3955 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" V 4305 4000 50  0001 C CNN
F 3 "~" H 4375 4000 50  0001 C CNN
	1    4375 4000
	1    0    0    -1  
$EndComp
Text Label 4375 3675 0    50   ~ 0
1V8
Wire Wire Line
	4375 3675 4375 3850
$EndSCHEMATC
