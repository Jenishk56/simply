ping google.com -c 1 | grep round-trip | cut -d '=' -f 2 | cut  -d '/' -f 1