# TODO: is there an easier way to do this?
def parse_client_files(data):
    return data[0].replace("\n", "")

with open("clientsecret", "r") as f:
    clientsecret = parse_client_files(f.readlines())

with open("clientid", "r") as f:
    clientid = parse_client_files(f.readlines())

CLIENT_SECRET = clientsecret
CLIENT_ID = clientid

# FIXME: make dependent on environment
BASE_URL = "localhost:5000"
