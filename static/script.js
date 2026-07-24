const sessionId = crypto.randomUUID();

async function sendMessage(){

    const input = document.getElementById("message");

    const chatBox = document.getElementById("chat-box");

    const text = input.value;

    if(text===""){

        return;
    }

    chatBox.innerHTML +=
    `<div class="message user">${text}</div>`;

    input.value="";

    const response = await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            session_id:sessionId,

            message:text

        })

    });

    const data = await response.json();

    chatBox.innerHTML +=
    `<div class="message bot">${data.reply}</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;
}
