import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav, Dropdown, NavItem, NavLink } from 'react-bootstrap';
import Conversation from './components/conversation';
import './custom-styles.css';

function App() {
    return (
        <div>
            <Navbar expand="lg" className="px-3 py-2 custom-bg-grenat">
                <Navbar.Brand href="#" style={{ color: 'white' }}>SimpliFair</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Dropdown title="Useful Links" id="basic-nav-dropdown" as={Nav.Item}>
                            <Dropdown.Toggle as={Nav.Link} style={{ color: 'white' }}>Useful links</Dropdown.Toggle>
                            <Dropdown.Menu>
                                <Dropdown.Item href="https://economie.fgov.be/en/themes/online/belmed-online-mediation/alternative-dispute-resolution/forms-dispute-resolution/conciliation/justices-peace" style={{ color: 'black' }}>Justices of the Peace</Dropdown.Item>
                                <Dropdown.Item href="https://economie.fgov.be/en/themes/online/belmed-online-mediation/alternative-dispute-resolution/extrajudicial-alternative" style={{ color: 'black' }}>Extrajudicial Alternative</Dropdown.Item>
                                <Dropdown.Item href="https://www.ombudsman.be/nl/ombudsman/domain/all" style={{ color: 'black' }}>Ombudsdman.be</Dropdown.Item>
                                <Dropdown.Item href="https://www.fbc-cfm.be/nl/inhoud/verzoening-voor-de-rechter" style={{ color: 'black' }}>Verzoening voor de rechter</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>

            {/* Container for main content */}
            <div className="container mt-3">
                {/* Title */}
                {/* <h1 className="text-center">Welcome to [Just'AIce<sup>3</sup>]</h1> */}
                {/* Conversation component */}
                <p>
                    Disclaimer: The information provided by this chatbot is for general informational purposes only. It should not be considered legal, medical, financial, or any other professional advice. You should not rely on the information provided by this chatbot as a substitute for professional advice or consultation. We are committed to protecting your privacy and personal data in accordance with the General Data Protection Regulation (GDPR) and other applicable data protection laws. Any personal information collected through this chatbot will be handled in accordance with our Privacy Policy. While we strive to provide accurate and up-to-date information, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability with respect to the chatbot or the information, products, services, or related graphics contained in the chatbot for any purpose. Any reliance you place on such information is therefore strictly at your own risk. In no event will we be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of this chatbot. Through this chatbot, you are able to link to other websites and resources which are not under the control of the chatbot owner. We have no control over the nature, content, and availability of those sites. The inclusion of any links does not necessarily imply a recommendation or endorse the views expressed within them. Every effort is made to keep the chatbot up and running smoothly. However, the chatbot owner takes no responsibility for, and will not be liable for, the chatbot being temporarily unavailable due to technical issues beyond our control. By using this chatbot, you consent to the terms of this disclaimer and agree to abide by them. If you do not agree to these terms, please refrain from using the chatbot.
                </p>
                <Conversation />
            </div>
        </div>
    );
}

export default App;