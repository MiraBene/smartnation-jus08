import React from "react";

import History from './history';
import Prompt from './prompt';

import api from '../api';

const Conversation = () => (
    <div class="">
        <h2 class="">Conversation</h2>
        <div>
            <p>Coucou je suis le chat !</p>
            <p>Bonjour le chat.</p>
            <p>Bonjour !</p>
        </div>
        <form>
            <input type="textarea" rows="4" cols="50" />
            <input type="submit" value="Submit" />
        </form>
    </div>
);

export default Conversation;