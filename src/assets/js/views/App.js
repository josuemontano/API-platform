import { Router, route } from 'preact-router';
import { isAuthenticated } from '~/utils/auth';
import { h, Component } from 'preact';

import LoginForm from './LoginForm';
import Welcome from './Welcome';

export default class App extends Component {
  static onRouteChanged(event) {
    const { url } = event;
    if (url !== '/login' && !isAuthenticated()) {
      route('/login', true);
    }
  }

  render() {
    return (
      <Router onChange={App.onRouteChanged}>
        <Welcome path="/" />
        <LoginForm path="/login" googleClientID={window.googleClientID} windowsClientID={window.windowsClientID} />
      </Router>
    );
  }
}
