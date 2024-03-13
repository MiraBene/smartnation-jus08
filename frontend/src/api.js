import axios from 'axios';

// Backend address is specified in the package.json ("proxy" attribute)
const api = axios.create();

export default api;
