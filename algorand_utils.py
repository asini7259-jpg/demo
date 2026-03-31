from algosdk.v2client import algod

client = algod.AlgodClient("", "https://testnet-api.algonode.cloud")

def verify_transaction(txn_id):
    try:
        tx = client.pending_transaction_info(txn_id)
        return tx.get("confirmed-round", 0) > 0
    except:
        return False