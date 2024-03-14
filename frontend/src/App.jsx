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
                <p>Les réponses fournies dans le cadre de cette conversation sont fournies par une I.A. etc.</p>
                <Conversation />
            </div>
        </div>
    );
}

export default App;