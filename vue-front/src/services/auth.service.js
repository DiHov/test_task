import api from './api';
import TokenService from './token.service';

const API_URL = 'http://localhost:8000/';

class AuthService {
  login(user) {
    return api
      .post(API_URL + 'signin/', {
        id: user.id,
        password: user.password
      })
      .then(response => {
        if (response.data.access) {
          TokenService.setUser(response.data);
        }

        return response.data;
      });
  }

  logout() {
    TokenService.removeUser();
  }

  register(user) {
    return api.post(API_URL + 'signup/', {
      id: user.id,
      password: user.password
    });
  }
}

export default new AuthService();