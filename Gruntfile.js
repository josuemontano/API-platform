'use strict';

module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt);
    require('time-grunt')(grunt);

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            sass: {
                files: 'client/assets/scss/*.scss',
                tasks: ['sass', 'copy']
            },
            browserify: {
                files: ['client/js/app/**/*.coffee', 'client/js/app/**/*.hbs'],
                tasks: ['browserify', 'uglify']
            }
        },
        browserSync: {
            dev: {
                bsFiles: {
                    src : [
                        '<%= pkg.name %>/static/css/*.css',
                        '<%= pkg.name %>/static/js/*.min.js',
                    ]
                },
                options: {
                    watchTask: true,
                    proxy: '127.0.0.1:6543'
                }
            }
        },
        browserify: {
            dist: {
                files: {
                    '<%= pkg.name %>/static/js/<%= pkg.name %>.js': ['client/js/app/**/*.coffee'],
                },
                options: {
                    browserifyOptions: {
                        extensions: ['.coffee', '.hbs']
                    },
                    transform: [
                        'coffeeify',
                        ['hbsfy', {
                            processContent: function(content) {
                                // content = content.replace(/^[\x20\t]+/mg, '').replace(/[\x20\t]+$/mg, '');
                                // content = content.replace(/^[\r\n]+/, '').replace(/[\r\n]*$/, '\n');
                                return content;
                            }
                        }],
                        'uglifyify'
                    ],
                }
            },
        },
        uglify: {
            options: {
                sourceMap: true,
                banner: '/**' +
                        '\n * <%= pkg.name %>' +
                        '\n * @version <%= pkg.version %>' +
                        '\n * @date <%= grunt.template.today("dd-mm-yyyy") %>' +
                        '\n**/\n'
            },
            dist: {
                files: {
                    '<%= pkg.name %>/static/js/<%= pkg.name %>.min.js': ['<%= pkg.name %>/static/js/<%= pkg.name %>.js']
                }
            }
        },
        sass: {
            dist: {
                options: {
                    style: 'compressed',
                    sourcemap: 'none',
                },
                files: [{
                    expand: true,
                    cwd: 'client/assets/scss',
                    src: ['*.scss'],
                    dest: '<%= pkg.name %>/static/css',
                    ext: '.min.css'
                }]
            }
        },
        copy: {
            main: {
                files: [{
                    cwd: 'client/assets/img',
                    src: ['**/*'],
                    dest: '<%= pkg.name %>/static/img',
                    expand: true
                }, {
                    cwd: 'client/assets/css',
                    src: ['**/*'],
                    dest: '<%= pkg.name %>/static/css',
                    expand: true
                }]
            }
        },
        coffeelint: {
            app: ['client/js/app/**/*.coffee'],
            options: {
                'max_line_length': {
                  'level': 'warn'
                }
            }
        },
        karma: {
            unit: {
                configFile: 'karma.conf.js'
            }
        }
    });

    grunt.registerTask('default', [
        'browserSync',
        'watch'
    ]);

    grunt.registerTask('build', [
        'copy',
        'sass',
        'coffeelint',
        'browserify',
        'uglify',
    ]);
};
