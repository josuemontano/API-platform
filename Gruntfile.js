module.exports = function (grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        
        // Watch task config
        watch: {
            sass: {
                files: "<%= pkg.name %>/scss/*.scss",
                tasks: ['sass']
            }
        },
        // SASS task config
        sass: {
            dist: {
                options: {
                    style: 'compressed',
                    sourcemap: 'none',
                },
                files: {
                    "<%= pkg.name %>/static/css/theme.min.css" : "<%= pkg.name %>/scss/theme.scss"
                }
            }
        },

        concat: {
            options: {
                separator: ';'
            },
            dist: {
                src: ['<%= pkg.name %>/static/js/**/*.js'],
                dest: '<%= pkg.name %>/static/js/<%= pkg.name %>.js'
            }
        },

        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
            },
            dist: {
                files: {
                    '<%= pkg.name %>/static/js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
                }
            }
        },
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('default', ['sass', 'concat', 'uglify']);
};
