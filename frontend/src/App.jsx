import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import Conversation from './components/conversation';

function App() {
    return (
        <div>
            <Navbar bg="success" expand="lg" className="px-3 py-2">
                <Navbar.Brand href="#" style={{ color: 'white' }}>J.U.S. #08</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link href="https://economie.fgov.be/en/themes/online/belmed-online-mediation/alternative-dispute-resolution/forms-dispute-resolution/conciliation/justices-peace" style={{ color: 'white' }}>Justices of the Peace</Nav.Link>
                        <Nav.Link href="https://economie.fgov.be/en/themes/online/belmed-online-mediation/alternative-dispute-resolution/extrajudicial-alternative" style={{ color: 'white' }}>Extrajudicial Alternative</Nav.Link>
                        <Nav.Link href="https://www.ombudsman.be/nl/ombudsman/domain/all" style={{ color: 'white' }}>Ombudsdman.be</Nav.Link>
                        <Nav.Link href="https://www.fbc-cfm.be/nl/inhoud/verzoening-voor-de-rechter" style={{ color: 'white' }}>Verzoening voor de rechter</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>

            {/* Container for main content */}
            <div className="container mt-3">
                {/* Title */}
                <h1 className="text-center">Welcome to J.U.S. #08</h1>
                {/* Conversation component */}
                <Conversation />
            </div>
        </div>
    );
}

export default App;