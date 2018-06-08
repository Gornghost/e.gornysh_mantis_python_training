from model.project import Project
import getopt
import sys
import jsonpickle
import os.path
import random
import string


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number_of_groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols).strip() for i in range(random.randrange(maxlen))])


def random_status():
    symbols = ["development", "release", "stable", "obsolete"]
    return "".join([random.choice(symbols).strip()])


def random_view_status():
    symbols = ["public", "private"]
    return "".join([random.choice(symbols).strip()])


testdata = [
    Project(name=random_string("name", 10), status=random_status(), description=random_string("description", 40), view_status=random_view_status())
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))