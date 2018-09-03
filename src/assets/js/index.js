import '@babel/polyfill';
import 'uikit';
import { h, render } from 'preact';

import 'uikit/dist/css/uikit.min.css';
import '../css/theme.scss';


let root;

function init() {
  let App = require('./views/App').default;
  root = render(<App />, document.body, root);
}

init();

// Re-render on Webpack HMR update:
if (module.hot) module.hot.accept('./views/App', init);
