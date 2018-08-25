import axios from 'axios';


function storeUserCredentials(user, accessToken) {
  const crendentials = {
    id: user.id,
    access_token: accessToken,
  };
  localStorage.setItem('user', JSON.stringify(crendentials));
}

export function getUserCredentials() {
  return JSON.parse(localStorage.getItem('user')) || {};
}

export function onLogin(user, accessToken) {
  storeUserCredentials(user, accessToken);
  window.location = '/';
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
