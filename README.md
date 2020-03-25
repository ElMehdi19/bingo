Command line parameters:

    $ python app.py -h
    
    positional arguments:
    -h, --help            show this help message and exit
    -i IP, --ip IP        Server's IP address
    -w FILE, --file FILE  True to save results in a txt file

### Note: Argument **-i** is required.

Usage:

    $ python app.py -i 127.0.0.1 -w True

Output:

    http://domain1.com
    http://domain2.com
    http://sub.domain1.com

    _____________________________

    {number of domains} websites found in {ip address}

### Note: Argument **-w** is optional, but in order to write the results to a txt file It **must** be set to **True**
