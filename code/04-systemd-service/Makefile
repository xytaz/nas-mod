all:
	sudo cp nas.service /lib/systemd/system/
	sudo chmod 644 /lib/systemd/system/nas.service
	sudo systemctl daemon-reload
	sudo systemctl enable nas.service
	# Reboot
	# shutdown -r now