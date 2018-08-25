import hello from 'hellojs';
import { authenticate } from '~/utils/auth';
import { h, Component } from 'preact';

export default class LoginForm extends Component {
  constructor(props) {
    super(props);

    hello.init(
      {
        google: props.googleClientID,
        windows: props.windowsClientID,
      },
      {
        display: 'page',
        page_uri: window.location.href,
        redirect_uri: '/login',
      },
    );

    this.loginUserOnRedirect();
  }

  static onGoogleLogin() {
    const provider = hello('google');
    provider.login({ scope: 'openid, email', force: true });
  }

  static onWindowsLogin() {
    const provider = hello('windows');
    provider.login({ scope: 'email', force: true });
  }

  loginUserOnRedirect() {
    // Login user on redirection
    let authResponse = hello('google').getAuthResponse();
    if (!authResponse) authResponse = hello('windows').getAuthResponse();

    if (authResponse) authenticate(authResponse);
  }

  render() {
    return (
      <p uk-margin>
        <button type="button" onClick={LoginForm.onGoogleLogin} class="uk-button uk-button-primary">
          Entrar con Google
        </button>
        <button type="button" onClick={LoginForm.onWindowsLogin} class="uk-button uk-button-secondary">
          Entrar con Microsoft
        </button>
      </p>
    );
  }
}
