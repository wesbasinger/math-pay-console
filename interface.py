from json import load
from block_io import BlockIo

from pymongo import MongoClient

import csv

version = 2

with open('secret.json') as f:

    data = load(f)

block_io = BlockIo(
    data['API_KEY'],
    data['SECRET_PIN'],
    version
)

def create_new_label(label):

    result = block_io.get_new_address(label=label)

    if(result['status'] == 'success'):

        print(f'Address for {label} created successfully.')

    else:

        print("Error occurred while creating address.")

def deposit(label, amount):

    try:

        result = block_io.withdraw_from_labels(
            amounts=amount,
            from_labels="default",
            to_labels=label
        )

    except:

        print(f'Address for {label}  does not exist, creating one now.')

        create_new_label(label)

        result = block_io.withdraw_from_labels(
            amounts=amount,
            from_labels="default",
            to_labels=label
        )

    if(result['status'] == 'success'):

        print(f'Amount of {amount} successfully sent to {label}.')

    else:

        print("Error occured while sending amount.")

def pay_ledger():

    with open('ledger.csv') as csvfile:

        reader = csv.DictReader(csvfile)

        if("Email" not in reader.fieldnames or "Payment" not in reader.fieldnames):

            print("File error!  Check headers.")

        else:

            for row in reader:

                if (int(row['Payment']) < 2):

                    print("Skipping deposit, amount is less than 2.")

                else:

                    deposit(row['Email'], row['Payment'])

def create_new_bounty(teaser, ptext, answer, instructions, imgLink):

    doc = {
        "teaser" : teaser,
        "ptext" : ptext,
        "answer" : int(answer),
        "instructions" : instructions,
        "imgLink" : imgLink,
        "solved" : False,
        "reward" : 10
    }

    MONGO_URI = data['MONGO_URI']

    client = MongoClient(MONGO_URI, ssl=True)

    db = client['mathpay']

    bounties = db.bounties

    result = bounties.insert_one(doc)

    if result:

        print("Bounty added successfully.")

    else:

        print("Error occured.")
