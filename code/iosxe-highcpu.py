import cli

timestamp = cli.execute("show clock")
processes = cli.execute("show proc cpu sort")
histogram = cli.execute("show proc cpu hist")
users = cli.execute("show users")

fp = open('/bootflash/highcpulog.txt','w')
fp.write("High CPU at "+timestamp+"\n\n")

processlines = processes.splitlines()
fp.write("CPU and top ten processes:\n\n")
for x in range(0,12):
    fp.write(processlines[x]+"\n")
fp.write("CPU histogram:\n\n")
fp.write(histogram+"\n\n")
fp.write("Active users:\n\n")
fp.write(users+"\n\n")
fp.close()

topproc = processlines[2][65:]
cli.execute("send log 3 High CPU detected. Check /bootflash/highcpulog.txt : Top process: "+topproc)
