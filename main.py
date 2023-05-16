import os
import argparse
from getpass import getpass  # For interactive password input

def pkg_install(pkg_name):
    installed = False
    while not installed:
        try:
            __import__(pkg_name)
            installed = True
        except ImportError:
            try:
                os.system(f"pip install -U {pkg_name}")
                installed = True
            except:
                os.system(f"pip3 install -U {pkg_name}")
                installed = True

    return True

if __name__ == "__main__":

    assert(pkg_install('hypebankapi'))
    from hypebankapi import Hype, utils

    parser = argparse.ArgumentParser(
        prog="HypeBankAPI",
        description='Fetch data from Hype API and create JSON folder with profile, balance, card and movements information'
    )
    parser.add_argument('-m', '--email', help='Email address', required=True, type=str)
    parser.add_argument('-b', '--birthdate', help='Birth date in ISO (YYYY-MM-DD)', required=True)
    parser.add_argument('-l', '--limit', help='Limit the number of transactions to fetch from Hype API. Default to 50', required=False, default=50, type=int)
    parser.add_argument('-v', '--verbose', action='store_true', required=False, default=False)
    args = parser.parse_args()

    h = Hype()
    h.login(args.email, getpass('Hype password: '), args.birthdate)
    if args.verbose:
        print('Logged in. Waiting for OTP code...\n')

    # Wait for OTP code to arrive via SMS
    h.otp2fa(input("OTP code: "))

    # You are now logged in
    profile = h.get_profile()
    balance = h.get_balance()
    card = h.get_card()
    movements = h.get_movements(limit=args.limit)

    utils.save_json(profile, 'profile.json')
    utils.save_json(balance, 'balance.json')
    utils.save_json(card, 'card.json')
    utils.save_json(movements, 'movements.json')
    if args.verbose:
        print('JSON folder created.\nNow you can run the Streamlit WebApp!')