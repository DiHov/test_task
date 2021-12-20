import api from './api';

const API_URL = 'http://localhost:8000/';

class UserService {
  getPublicContent() {
    return api.get(API_URL + 'latency');
  }
  getInfo() {
    return api.get(API_URL + 'info');
  }

}

export default new UserService();