class Chatbox {
    constructor(){

        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            voiceButton: document.querySelector('.voice__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton, voiceButton} = this.args;
        
        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        voiceButton.addEventListener('click', () => this.onVoiceButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key:string}) => {
            if (key === 'Enter'){
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox){
        this.state = !this.state;
        // show or hides the box
        if (this.state) {
            chatbox.classList.add('chatbox--active')
            fetch("http://192.168.1.2:3000/welcome", {
                method: 'POST',
                body: JSON.stringify(),
                mode: 'cors',
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            .then(r => r.json())
            .then(r => {
                let msg = {name: "Sam", message: r};

                // this.text2speak(msg.message)
                console.log(msg.message)
                this.messages.push(msg);
                this.updateChatText(chatbox)
            }).catch((error) => {
                console.log('Error: ', error);
                this.updateChatText(chatbox)
            });
        }
        else{
            chatbox.classList.remove('chatbox--active');
        }
    }

    onSendButton(chatbox){
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 == ""){
            return;
        }

        let msg1 = {name: "User", message: text1}
        this.messages.push(msg1);
        // 'http://127.0.0.1:5000/predict
        fetch($SCRIPT_ROOT + "/predict", {
            method: 'POST',
            body: JSON.stringify({message: text1}),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(r => r.json())
        .then(r => {
            let msg2 = {name: "Sam", message: r.answer};
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''
        }).catch((error) => {
            console.error('Error: ', error);
            this.updateChatText(chatbox)
            textField.value = ''
        });
    }

    onVoiceButton(chatbox){
        // // var textField = chatbox.querySelector('input');
        let text1 = "Say somehting ..."
        // // // if (text1 == ""){
        // // //     return;
        // // // }

        let msg1 = {name: "Sam", message: text1}
        this.messages.push(msg1);
        this.updateChatText(chatbox)
        // 'http://127.0.0.1:5000/voice_predict
        fetch($SCRIPT_ROOT + "/voice_predict", {
            method: 'POST',
            body: JSON.stringify({message: text1}),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(r => r.json())
        .then(r => {
            // let msg1 = {name: "Sam", message: r.question}
            // this.messages.push(msg1)
            let msg2 = {name: "Sam", message: r.answer};
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''
        }).catch((error) => {
            console.error('Error: ', error);
            this.updateChatText(chatbox)
            textField.value = ''
        });
    }

    updateChatText(chatbox){
        var html = '';
        this.messages.slice().reverse().forEach(function(item, number){
            if (item.name==="Sam"){

            html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
        }
        else
        {
            html += '<div class="messages__item messages_item--operator">' + item.message + '</div>'
        }
    });

    const chatmessage = chatbox.querySelector('.chatbox__messages');
    chatmessage.innerHTML = html;
    }
}

const chatbox = new Chatbox();
chatbox.display()