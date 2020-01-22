# Standard modules
from subprocess import Popen, PIPE
from datetime import datetime

class CLI:
  network_interface = None

  # The following functions are borrowed from Adafruit with little to no modification.
  # Reference: https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi?view=all
  # >>>
  def run_cmd(cmd: 'str - A valid Linux terminal command'):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

  def find_network_interface():
    find_device = "ip addr show"
    interface_parse = CLI.run_cmd(find_device)
    dev_name = None
    for line in interface_parse.splitlines():
      if "state UP" in line:
        dev_name = line.split(':')[1]
    return dev_name

  def parse_ip(version: 'str - Either "ipv4" or "ipv6"'):
    CLI.network_interface = CLI.find_network_interface()

    find_ip = f'ip addr show {CLI.network_interface}'
    ip_parse = CLI.run_cmd(find_ip)

    for line in ip_parse.splitlines():
      if version == 'ipv4' and 'inet' in line:
        ip = line.split(' ')[5]
        ip = ip.split('/')[0]
        return ip
      elif version == 'ipv6' and ('inet6' in line and 'global' in line):
        ipv6 = line.split(' ')[5]
        ipv6 = ipv6.split('/')[0]
        return ipv6
  # <<<

  def get_ip():
    return CLI.parse_ip('ipv4')

  def get_ipv6():
    return CLI.parse_ip('ipv6')

  def get_network_ssid():
    cmd = 'iwgetid'
    ssid_parse = CLI.run_cmd(cmd)
    ssid_name = None
    if (len(ssid_parse) == 0):
      ssid_name = 'None'
    else:
      for line in ssid_parse.splitlines():
        if 'ESSID' in line:
          ssid_name = line.split('"')[1]
    return ssid_name

  def get_cpu_temp():
    cmd = 'cat /sys/class/thermal/thermal_zone*/temp'
    temp_parse = CLI.run_cmd(cmd)
    temp_parse = temp_parse.splitlines()
    temp = None

    cmd = 'cat /sys/class/thermal/thermal_zone*/type'
    temp_label_parse = CLI.run_cmd(cmd)
    temp_label_parse = temp_label_parse.splitlines()
    label = None

    results = []
    for i in range(0, len(temp_parse)):
      t = temp_parse[i].strip()
      t = int(t) / 1000
      t = '{:0.1f}'.format(t)
      item = temp_label_parse[i].split('-')[0] + ': ' + t
      results.append(item)
    return results

  def get_disk_usage():
    cmd = 'df --output=pcent,source'
    disk_parse = CLI.run_cmd(cmd)
    disk_info_list = []
    for line in disk_parse.splitlines():
      if '/dev/sd' in line or '/dev/mmc' in line:
        line_list= line.split('/')
        disk_name = line_list[2]
        disk_usage = line_list[0]
        disk_info_list.append(f'{disk_name}: {disk_usage}')
    if (len(disk_info_list) == 0):
      disk_info_list.append('None')
    return disk_info_list

  def get_hostname():
    cmd = 'hostname'
    results = CLI.run_cmd(cmd)
    return results.strip()

  def get_datetime():
    return datetime.now().strftime('%b %d  %H:%M:%S')