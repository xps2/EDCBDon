# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from ConfigParser import ConfigParser
from mastodon import Mastodon
import sys
from win32api import GetDiskFreeSpaceEx

parser = ArgumentParser(
    prog="EDCBDon"
)
group = parser.add_mutually_exclusive_group()
group.add_argument('-t', '--token',
    action='store_true',
    help='get access token'
)
group.add_argument('toot',
    action='store',
    nargs='?',
    help='toot'
)
parser.add_argument('--hdd',
    action='store',
)


def get_access_token():
    config = ConfigParser()
    config.readfp(open('token.ini'))

    section = 'Token'
    api_base_url = config.get(section, 'api_base_url')
    username = config.get(section, 'username')
    password = config.get(section, 'password')

    client_id = 'edcbdon_clientcred.secret'
    access_token = 'edcbdon_usercred.secret'
    scopes = ['read', 'write']

    Mastodon.create_app(
         'EDCBDon',
         scopes=scopes,
         api_base_url=api_base_url,
         to_file=client_id
    )

    mastodon = Mastodon(
        client_id=client_id,
        api_base_url=api_base_url
    )

    mastodon.log_in(
        username=username,
        password=password,
        scopes=scopes,
        to_file=access_token
    )


def toot(toot_str, hdd_path):
    config = ConfigParser()
    config.readfp(open('edcbdon.ini'))
    section = 'EDCBDon'

    if hdd_path is not None:
        print hdd_path
        hdd = GetDiskFreeSpaceEx(hdd_path)
        toot_str = toot_str + u" 空き容量: {:.2f}".format(hdd[0] / (1024.0 ** 3)) + "GB"

    mastodon = Mastodon(
        client_id='edcbdon_clientcred.secret',
        access_token='edcbdon_usercred.secret',
        api_base_url=config.get(section, 'api_base_url')
    )

    mastodon.toot(toot_str)

def main():
    args = parser.parse_args(sys.argv[1:])
    
    if args.token:
        get_access_token()
        sys.exit(0)
    elif args.toot:
        toot(unicode(args.toot, 'cp932'), args.hdd)
    
if __name__ == '__main__':
    main()