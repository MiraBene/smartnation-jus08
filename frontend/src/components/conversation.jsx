import React, { useState } from "react";

//import api from '../api';
import axios from 'axios';
import '../custom-styles.css';

const Conversation = () => {
    const [messages, setMessages] = useState([]);
    const [isWaiting, setIsWaiting] = useState(false);

    const getChatAnswer = async (query) => {
        setIsWaiting(true);
        try {
            const requestBody = {
                content: query
            };

            //const response = await api.post("/get_answer", requestBody);
            const response = await axios.post("http://0.0.0.0:8000/get_answer", requestBody);

            const data = await response.data;
            if (response.status === 200) {
                setMessages(prevMessages => [data.content, ...prevMessages]);
            }
        } catch (error) {
            console.error("Error feteching data!")
        } finally {
            setIsWaiting(false);
        }
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        const newMessage = event.target.elements[0].value;
        setMessages(prevMessages => [newMessage, ...prevMessages]);
        getChatAnswer(newMessage);
        event.target.reset();
    };

    return (
        <div className="border rounded p-3 mb-3 d-flex flex-column" style={{ maxHeight: '80vh', overflowY: 'auto' }}>
            <h2 className="text-center mb-4">Conversation</h2>
            <div className="flex-grow-1 overflow-auto">
                {/* Messages div*/}
                {/* Messages are stylised alternatively: odd messages belong to the user, even messages to the chatbot. */}
                <div className="d-flex flex-column-reverse">
                    {messages.slice().map((message, index) => (
                        <div key={index} className={index % 2 === 0 ?
                            "align-self-start custom-bg-linen rounded p-1 mb-2" :
                            "align-self-end custom-bg-salmon rounded p-1 mb-2"
                        }>
                            <p className="px-2 m-0">{message}</p>
                        </div>
                    ))}
                </div>
            </div>
            <form onSubmit={handleSubmit} className="mt-auto">
                <textarea rows="4" cols="50" className="form-control mb-2" />
                { }
                <button type="submit" className={isWaiting ? "btn custom-bg-grenat" : "btn custom-bg-salmon"} disabled={isWaiting}>
                    {isWaiting ? 'Please wait...' : 'Submit'}
                </button>
            </form>
        </div>
    );
};

export default Conversation;
