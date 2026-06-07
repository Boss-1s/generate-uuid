"""UUIDv1,3,4,5,6 generation for gh actions"""
import os
import uuid
import warnings

VERSION = os.environ.get("INPUT_VERSION")
namespace = os.environ.get("INPUT_NAMESPACE")
name = os.environ.get("INPUT_NAME")

UUIDTYP = getattr(uuid, f"uuid{VERSION}")
OUTPUT = ""

versions = ["1", "3", "4", "5", "6"]
namespaces = ["DNS", "URL", "OID", "X500"]

def print_in_os(argument):
    "print in both terminal and action logs"
    print(f"{argument}")
    os.system(f"echo {argument}")

print_in_os(f"Version: {VERSION}")

if VERSION in versions or namespace in namespaces:
    if VERSION in ["3", "5"]:
        match namespace:
            case "DNS":
                namespace = uuid.NAMESPACE_DNS
            case "URL":
                namespace = uuid.NAMESPACE_URL
            case "OID":
                namespace = uuid.NAMESPACE_OID
            case "X500":
                namespace = uuid.NAMESPACE_X500
            case _:
                raise ValueError(f"ERROR: namespace cannot be '{namespace}'; must be either DNS, URL, OID, "
                          + "or X500.")
        print(namespace)
        OUTPUT = UUIDTYP(name, fb"{namespace}")
    else:
        if namespace or name:
            warnings.warn("No namespace or name needed for this version",
                          UserWarning)
        OUTPUT = UUIDTYP()
else:
    if not namespace in namespaces and namespace > "":
        raise ValueError(f"ERROR: namespace cannot be '{namespace}'; must be either DNS, URL, OID, "
                          + "or X500.")
    else:
        if not VERSION in versions and VERSION > "":
            raise ValueError(f"ERROR: VERSION {VERSION} does not exist")

OUTPUTSTR = str(OUTPUT)
FINAL = uuid.UUID(OUTPUTSTR)
SAFE = uuid.SafeUUID

os.system(f"echo 'uuid={FINAL}' >> $GITHUB_OUTPUT")
os.system(f"echo 'safe={SAFE}' >> $GITHUB_OUTPUT")

if SAFE == "unsafe":
    print_in_os("::warning title=UNSAFE::Your UUID may be unsafe for public use because" +
                " it may contain some of your device's personal info.")
