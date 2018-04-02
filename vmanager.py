import sys


def usage():
    print("Virtual machines manager")
    print("vmanager.py deploy <hostname>")
    print("vmanager.py halt <hostname>")
    print("vmanager.py start <hostname>")
    print("vmanager.py destroy <hostname>")


def deploy(hostname):
    print("You are trying to deploy the machine with the hostname " + hostname)


def halt(hostname):
    print("You are trying to halt the machine with the hostname " + hostname)


def start(hostname):
    print("You are trying to start the machine with the hostname " + hostname)


def destroy(hostname):
    print("You are trying to destroy the machine with the hostname " + hostname)


if __name__ == "__main__":

    if len(sys.argv) <= 2:
        usage()
    else:
        if sys.argv[1] == "deploy":
            deploy(sys.argv[2])

        elif sys.argv[1] == "halt":
            halt(sys.argv[2])

        elif sys.argv[1] == "start":
            start(sys.argv[2])

        elif sys.argv[1] == "destroy":
            destroy(sys.argv[2])

        else:
            usage()
