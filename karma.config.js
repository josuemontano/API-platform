const baseKarmaConfig = require('./webpack.karma.config.js');

module.exports = function(config) {
  config.set({
    browsers: ['Chrome'],
    frameworks: ['mocha', 'sinon'],
    files: ['./tests/assets/spec_loader.js'],
    preprocessors: {
      './tests/assets/spec_loader.js': ['webpack'],
    },
    reporters: ['mocha'],
    mochaReporter: {
      showDiff: true,
    },
    webpack: baseKarmaConfig,
    webpackMiddleware: {
      stats: 'errors-only',
    },
  });
};
