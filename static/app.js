const $=id=>document.getElementById(id);
$("convertBtn").addEventListener("click",async()=>{
 const m=$("message");m.textContent="";m.className="message";
 try{
  const r=await fetch("/api/convert",{method:"POST",headers:{"Content-Type":"application/json"},
   body:JSON.stringify({number:$("number").value,base:$("base").value,bits:$("bits").value})});
  const d=await r.json();if(!r.ok)throw new Error(d.error);
  $("out2").value=d.binary;$("out8").value=d.octal;$("out10").value=d.decimal;$("out16").value=d.hexadecimal;
  m.textContent=`Conversión correcta. Máximo permitido: ${d.max_value}.`;m.className="message success";
 }catch(e){["out2","out8","out10","out16"].forEach(id=>$(id).value="");m.textContent=e.message;m.className="message error";}
});
document.querySelectorAll("[data-op]").forEach(b=>b.addEventListener("click",async()=>{
 try{
  const r=await fetch("/api/alu",{method:"POST",headers:{"Content-Type":"application/json"},
   body:JSON.stringify({a:$("aluA").value,b:$("aluB").value,operation:b.dataset.op})});
  const d=await r.json();if(!r.ok)throw new Error(d.error);$("aluResult").textContent=d.result;
 }catch(e){$("aluResult").textContent=e.message;}
}));
