# NAS Mod

## Auto-start script

### `systemd` service

Lastly, one of the ways to run a script on startup is by creating a `systemd` service.

See `/code/service/nas.service` for an example to use with the following steps.

1. Create a `<NAME>.service` file.
2. Copy to correct directory
```
sudo cp <NAME>.service /lib/systemd/system/
```
3. Change permissions
```
sudo chmod 644 /lib/systemd/system/<NAME>.service
```
4. Reload to register service
```
sudo systemctl daemon-reload
```
5. Enable service
```
sudo systemctl enable <NAME>.service
```
6. Reboot
```
sudo shutdown -r now
```

The service should be running. You can check by running `systemctl`.

In case something goes wrong, you can read the logs to debug. Python errors will show up here in the case the script fails at some point.
```
journalctl -u <NAME>.service
# You can also manage the service at any point
# sudo systemctl stop/start/restart <NAME>.service
```

If you decide to disable a service:
```
sudo systemctl disable <NAME>.service
```
Remember to remove service files in `/lib/systemd/system/` if you aim for complete deletion.

@CONFIRM Restart the service whenever you update the code (obviously), and also reload it (not so obvious).

### Helpful links:

- https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
- https://scruss.com/blog/2017/10/22/creating-a-systemd-user-service-on-your-raspberry-pi/
- https://unix.stackexchange.com/questions/225401/how-to-see-full-log-from-systemctl-status-service
- https://superuser.com/questions/513159/how-to-remove-systemd-services
- https://www.freedesktop.org/software/systemd/man/systemd.unit.html