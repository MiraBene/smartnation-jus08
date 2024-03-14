import React, { useState } from "react";

import api from '../api';

const Conversation = () => {
    const [messages, setMessages] = useState([]);

    const getChatAnswer = async (query) => {
        try {
            const requestBody = {
                content: query
            };

            const response = await api.post("/get_answer", requestBody);
            const data = await response.data;

            if (response.status === 200) {
                setMessages(prevMessages => [...prevMessages, data.content]);

            }
        } catch (error) {
            console.error("Error feteching data!")
        }
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        const newMessage = event.target.elements[0].value;
        setMessages(prevMessages => [...prevMessages, newMessage]);
        getChatAnswer(newMessage);
        event.target.reset();
    };

    return (
        <div className="border rounded p-3 mb-3">
            <h2 className="text-center mb-4">Conversation</h2>
            <div className="d-flex flex-column-reverse">
                {messages.slice().reverse().map((message, index) => (
                    <div key={index} className={index % 2 === 0 ? "align-self-end bg-light rounded p-2 mb-2" : "align-self-start bg-success text-white rounded p-2 mb-2"}>
                        <p className="m-0">{message}</p>
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit}>
                <textarea rows="4" cols="50" className="form-control mb-2" />
                <button type="submit" className="btn btn-success">Submit</button>
            </form>
        </div>
    );
};

export default Conversation;