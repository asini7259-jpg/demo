import React, { useState } from "react";
import axios from "axios";
import GraphView from "./GraphView";
import VoiceInput from "./VoiceInput";
import { connectWallet } from "./wallet";
import { sendPayment } from "./payment";

const API = "http://localhost:5000";

export default function App() {
  const [bill, setBill] = useState("");
  const [amt, setAmt] = useState("");
  const [acc, setAcc] = useState("");

  return (
    <div className="p-6 text-center">
      <h1 className="text-3xl">SplitPay 🚀</h1>

      <button onClick={async()=>setAcc(await connectWallet())}>
        Connect Wallet
      </button>

      <input placeholder="Bill ID" onChange={e=>setBill(e.target.value)} />
      <input placeholder="Amount" onChange={e=>setAmt(e.target.value)} />

      <button onClick={()=>axios.post(API+"/create-bill",
        {bill_id:bill,total:parseInt(amt),members:[acc]})}>
        Create
      </button>

      <button onClick={()=>sendPayment(acc)}>Pay</button>

      <VoiceInput setBill={setBill} setAmount={setAmt}/>
      <GraphView billId={bill}/>
    </div>
  );
}