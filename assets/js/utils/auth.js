import * as Cookies from 'js-cookie';
import axios from 'axios';
import { route } from 'preact-router';

function storeUserCredentials({ user, accessToken, expires }) {
  Cookies.set('crendentials', { user, accessToken }, { expires: new Date(expires) });
}

export function getUserCredentials() {
  return Cookies.getJSON('crendentials');
}

export function isAuthenticated() {
  const crendentials = getUserCredentials();
  return !(crendentials === null || crendentials === undefined);
}

export function onLogin(response) {
  storeUserCredentials(response);
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
    .then(onLogin)
    .catch((error) => {
      alert('User could not login');
      console.error(error);
    });
}
