import algosdk from "algosdk";
import { PeraWalletConnect } from "@perawallet/connect";

export async function sendPayment(sender){
  const client = new algosdk.Algodv2("", "https://testnet-api.algonode.cloud", "");

  const params = await client.getTransactionParams().do();

  const txn = algosdk.makePaymentTxnWithSuggestedParamsFromObject({
    from: sender,
    to: sender,
    amount: 1000000,
    suggestedParams: params
  });

  const pera = new PeraWalletConnect();
  const signed = await pera.signTransaction([[txn.toByte(),0]]);
  await client.sendRawTransaction(signed).do();
}