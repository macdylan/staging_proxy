# vim: set et fenc= ff=unix sts=4 sw=4 ts=4 :

import os
import re
import time
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = lambda *p: os.path.join(BASE_DIR, *p)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='host_file', type=argparse.FileType('r'),
        default=path('jumei_hosts.txt'),
        help='Specify which hosts file to read')
parser.add_argument('-o', '--output', dest='pac_file', type=argparse.FileType('w', 0),
        default=path('jumei_dev.pac'),
        help='Write output to <file>')
args = parser.parse_args()


ip_re = re.compile(r'[\.\:]')
useless_re = re.compile(r'^(?:\s*#+.+|\s*)$')

def generate_var(ip_str):
    return 'H_' + ip_re.sub('_', ip_str)

def make_rule(domain, proxy_var):
    return 'if (dnsDomainIs(host, "%s")) return %s;' % (domain, proxy_var)

def parse_hosts(fh):
    r = []
    t = None
    s = (' ', '\t')

    for line in args.host_file.readlines():
        if useless_re.search(line):
            continue

        if line[0] not in s:
            if t and t[1]: r.append(t[:])
            t = [None,[]] # [ip, [host1, host2, ...]]
            t[0] = line.strip()
        else:
            t[1].append(line.strip())

    if t and t[1]: r.append(t[:])

    return r

def pac_write(line, fh=None):
    if not fh:
        fh = args.pac_file
    fh.write( line + '\n' )

pac_write( '/* Last update: %s */' % time.asctime() )
pac_write( 'function FindProxyForURL(url, host) {' )
pac_write( '    if (isPlainHostName(host)) return "DIRECT";' )

rules = parse_hosts(args.host_file)
for ip, domains in rules:
   varname = generate_var(ip)
   if ':' not in ip: ip = ip + ':80'
   pac_write( '    var %s = "PROXY %s";' % (varname, ip) )
   for domain in domains:
       if domain[0] == '!':
           pac_write( '    if(dnsDomainIs(host, "%s")) return "DIRECT";' % domain[1:] )
       else:
           pac_write( '    if(dnsDomainIs(host, "%s")) return %s;' % (domain, varname) )

pac_write( '    return "DIRECT";' )
pac_write( '}' )

