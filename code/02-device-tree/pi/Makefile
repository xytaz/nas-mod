all:
	# 2. Compile
	dtc -O dtb -o nas-keys.dtbo nas-keys.dts
	dtc -O dtb -o nas-leds.dtbo nas-leds.dts
	dtc -O dtb -o nas-lcd.dtbo nas-lcd.dts
	
	# 3. Copy
	cp nas-keys.dtbo /boot/overlays/
	cp nas-leds.dtbo /boot/overlays/
	cp nas-lcd.dtbo /boot/overlays/

	# 4. Enable
	echo "" 				  >> /boot/config.txt
	echo "# NAS overlays" 	  >> /boot/config.txt
	echo "dtoverlay=nas-lcd"  >> /boot/config.txt
	echo "dtoverlay=nas-keys" >> /boot/config.txt
	echo "dtoverlay=nas-leds" >> /boot/config.txt

	# 5. Disable conflicting nodes
	sed -i 's/dtparam=i2c_arm=on/dtparam=i2c_arm=off/g' /boot/config.txt

	# 6. Reboot
	# shutdown -r now