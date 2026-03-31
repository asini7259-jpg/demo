import ForceGraph2D from "react-force-graph-2d";
import axios from "axios";
import { useEffect, useState } from "react";

export default function GraphView({billId}){
  const [data,setData]=useState({nodes:[],links:[]});

  useEffect(()=>{
    axios.get(`http://localhost:5000/settle/${billId}`)
    .then(res=>{
      const links=res.data.map(x=>({source:x.from,target:x.to,value:x.amount}));
      const nodes=[...new Set(links.flatMap(l=>[l.source,l.target]))].map(id=>({id}));
      setData({nodes,links});
    });
  },[billId]);

  return <ForceGraph2D graphData={data}/>
}