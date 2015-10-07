'use strict';

module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt);
    require('time-grunt')(grunt);

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            sass: {
                files: 'client/assets/scss/*.scss',
                tasks: ['sass']
            },
            angularjs: {
                files: 'client/app/**/*.js',
                tasks: ['concat', 'uglify']
            }
        },
        browserSync: {
            dev: {
                bsFiles: {
                    src : [
                        '<%= pkg.name %>/static/css/*.css',
                    ]
                },
                options: {
                    watchTask: true,
                    proxy: '127.0.0.1:6543'
                }
            }
        },
        jshint: {
            options: {
                jshintrc: '.jshintrc'
            },
            all: [
                'Gruntfile.js',
                'client/app/**/*.js',
            ]
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
        concat: {
            dist: {
                src: ['client/app/**/*.js'],
                dest: '<%= pkg.name %>/static/js/<%= pkg.name %>.js'
            }
        },
        uglify: {
            options: {
                banner: '/**' +
                        '\n * <%= pkg.name %>' +
                        '\n * @version <%= pkg.version %>' +
                        '\n * @date <%= grunt.template.today("dd-mm-yyyy") %>' +
                        '\n**/\n'
            },
            dist: {
                files: {
                    '<%= pkg.name %>/static/js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
                }
            }
        },
    });

    grunt.registerTask('default', [
        'browserSync',
        'watch'
    ]);
};
