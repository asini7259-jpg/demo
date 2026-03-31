export default function VoiceInput({setBill,setAmount}){
  const start=()=>{
    const rec=new window.webkitSpeechRecognition();

    rec.onresult=e=>{
      let t=e.results[0][0].transcript.split(" ");
      setBill(t[1]);
      setAmount(t[3]);
    };

    rec.start();
  };

  return <button onClick={start}>🎤 Speak</button>;
}