module.exports = function(config)
{
    config.set({
        frameworks: ['jasmine', 'browserify'],
        files: [
            'client/js/tests/**/*.coffee'
        ],
        reporters: [ 'dots' ],
        preprocessors: {
            'client/js/tests/**/*Spec.coffee': ['browserify']
        },
        browsers: [ 'PhantomJS' ],
        logLevel: config.LOG_ERROR,
        singleRun: true,
        autoWatch: false,
        browserify: {
            debug: true,
            extensions: ['.coffee', '.hbs'],
            transform: ['coffeeify', 'hbsfy']
        }
    });
};
