# Code based on:
# https://blog.sourcerer.io/writing-a-simple-linux-kernel-module-d9dc3762c234

# obj-m += hd44780.o
obj-m += ${NAME}.o
all:
	apt-get install build-essential
	apt-get install linux-headers-current-odroidxu4
	wget https://raw.githubusercontent.com/torvalds/linux/master/drivers/auxdisplay/charlcd.h
	wget https://raw.githubusercontent.com/torvalds/linux/master/drivers/auxdisplay/charlcd.c
	wget https://raw.githubusercontent.com/torvalds/linux/master/drivers/auxdisplay/hd44780.c

	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
	mkdir -p /lib/modules/$(shell uname -r)/kernel/drivers/auxdisplay/
	cp ${NAME}.ko /lib/modules/$(shell uname -r)/kernel/drivers/auxdisplay/

	# shutdown -r now
clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
test:
	# We put a — in front of the rmmod command to tell make to ignore
	# an error in case the module isn’t loaded.
	sudo rmmod ${NAME}
	# Clear the kernel log without echo
	sudo dmesg -C
	# Insert the module
	sudo insmod ${NAME}.ko
	# Display the kernel log
	dmesg