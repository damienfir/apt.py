import sys
import subprocess
from colored import Fore, Style


def print_usage():
    print("Usage: apt.py [--no-update] package_name")
    print("Arguments:")
    print("\t--no-update\tDon't update the cache")


def main():
    update = True
    target_name = None
    no_more = False

    for arg in sys.argv[1:]:
        if no_more:
            print("Too many arguments")
            print_usage()
            sys.exit(1)
        if arg == '--no-update':
            update = False
        else:
            target_name = arg
            no_more = True

    if not target_name:
        print("Expected package name")
        print_usage()
        sys.exit(1)

    if update:
        subprocess.run(["apt-get", "update"])


    process = subprocess.run(["apt-cache", "search", target_name], capture_output=True)

    package_info = {}
    for line in process.stdout.decode("utf-8").split("\n"):
        if not len(line):
            continue
        parts = [s.strip() for s in line.split(" - ")]
        package_info[parts[0]] = parts[1]

    names = package_info.keys()

    score = {}
    for p in names:
        if target_name in p:
            score[p] = len(p) - len(target_name)
        elif target_name in package_info[p]:
            score[p] = 100
        else:
            score[p] = 1000

    names_sorted = sorted(names, key=lambda x: score[x])

    package_list = {}
    for i, name in enumerate(reversed(names_sorted)):
        print(f"{Fore.blue}{len(names) - i}{Style.reset}: {Fore.green}{name}{Style.reset} - {package_info[name]}")
        package_list[len(names) - i] = name

    indices_string = input("Packages to install: ")
    if not len(indices_string):
        sys.exit(0)

    indices = [int(s) for s in indices_string.split()]
    names = [package_list[i] for i in indices]

    subprocess.run(["apt-get", "install"] + names)


try:
    main()
except KeyboardInterrupt:
    sys.exit(1)


# TODO: show if already installed
# TODO: basic tests
# TODO: handle sudo properly
