import * as Cookies from 'js-cookie';
import axios from 'axios';
import { route } from 'preact-router';


function storeUserCredentials(user, accessToken) {
  Cookies.set('crendentials', {
    id: user.id,
    access_token: accessToken,
  });
}

export function getUserCredentials() {
  return Cookies.getJSON('crendentials');
}

export function isAuthenticated() {
  const crendentials = getUserCredentials();
  return !(crendentials === null || crendentials === undefined);
}

export function onLogin(user, accessToken) {
  storeUserCredentials(user, accessToken);
  route('/', true);
}

export function logout() {
  Cookies.remove('crendentials');
  route('/login', true);
}

export function authenticate(params = {}) {
  axios
    .post(`/auth/${params.network}`, { access_token: params.access_token })
    .then(response => response.data)
    .then(response => onLogin(response.user, response.access_token))
    .catch((error) => {
      alert('User could not login');
    });
}
