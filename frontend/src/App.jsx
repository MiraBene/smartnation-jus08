// import './App.css';

import Conversation from './components/conversation';

function App() {
    return (
        <div>
            <h1>Welcome to J.U.S. #08</h1>
            <h2>Liens cools</h2>
            <ul>
                <li><a href="https://economie.fgov.be/en/themes/online/belmed-online-mediation/alternative-dispute-resolution/forms-dispute-resolution/conciliation/justices-peace">Justices of the Peace</a></li>
                <li><a href="https://economie.fgov.be/en/themes/online/belmed-online-mediation/alternative-dispute-resolution/extrajudicial-alternative">https://www.fbc-cfm.be/nl/inhoud/verzoening-voor-de-rechter</a></li>
                <li><a href="https://www.ombudsman.be/nl/ombudsman/domain/all">Ombudsdman.be</a></li>
                <li><a href="https://www.fbc-cfm.be/nl/inhoud/verzoening-voor-de-rechter">Verzoening voor de rechter</a></li>
            </ul>
            <Conversation />
        </div>
    );
}

export default App;
