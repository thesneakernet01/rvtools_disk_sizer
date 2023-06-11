This project was designed to take standard RVTools output and add up the
disk values from vPartition, vInfo and vDisk.  To help with sizing backup 
solutions for VMWare.

I built this using Anaconda for package management.  Anaconda can be downloaded from here: https://www.anaconda.com/download/
After that is installed, clone the git repo go into the folder, create an environment in conda from the environments yaml and then just run they python.
Script will ask for the file path to your rvtools dump.  Make sure there are no spaces in the RVTools dump file name. Because I'm lazy...

Output looks like the following:

vPartition indicates we have 18 TB of Disk Consumed
vDisk indicates we have 79 TB of Disk Provisioned
vinfo indicates we have 74 TB of in use Disk
vinfo indicates we have 81 TB of Provisioned Disk
