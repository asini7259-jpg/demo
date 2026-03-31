import { PeraWalletConnect } from "@perawallet/connect";

const pera = new PeraWalletConnect();

export async function connectWallet(){
  const acc = await pera.connect();
  return acc[0];
}