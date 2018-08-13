from json import load
from block_io import BlockIo

version = 2

with open('secret.json') as f:

    data = load(f)

block_io = BlockIo(
    data['API_KEY'],
    data['SECRET_PIN'],
    version
)

print(block_io.get_my_addresses())
