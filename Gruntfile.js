'use strict';

module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt);
    require('time-grunt')(grunt);

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            sass: {
                files: '<%= pkg.name %>/static/scss/**/*.scss',
                tasks: ['sass']
            },
            angularjs: {
                files: '<%= pkg.name %>/static/js/app/**/*.js',
                tasks: ['concat', 'uglify']
            }
        },
        browserSync: {
            dev: {
                bsFiles: {
                    src : [
                        '<%= pkg.name %>/static/css/*.css',
                        '<%= pkg.name %>/static/**/*.html',
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
                '<%= pkg.name %>/static/js/app/**/*.js',
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
                    cwd: '<%= pkg.name %>/static/scss',
                    src: ['*.scss'],
                    dest: '<%= pkg.name %>/static/css',
                    ext: '.min.css'
                }]
            }
        },
        concat: {
            options: {
                separator: ';'
            },
            dist: {
                src: ['<%= pkg.name %>/static/js/app/**/*.js'],
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
