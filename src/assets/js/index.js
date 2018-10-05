import '@babel/polyfill';
import 'uikit';
import { h, render } from 'preact';

import 'uikit/dist/css/uikit.min.css';
import '../css/theme.scss';


let root;

function init() {
  const App = require('./views/App').default;
  root = render(<App />, document.body, root);
}

// Re-render on Webpack HMR update:
if (module.hot) {
  __webpack_public_path__ = 'http://localhost:8080/';

  module.hot.accept();
  module.hot.accept('./views/App', init);
}

init();
