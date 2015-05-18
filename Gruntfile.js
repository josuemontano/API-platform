module.exports = function (grunt) {
    grunt.initConfig({
    // Watch task config
    watch: {
        sass: {
            files: "demonstrare/scss/*.scss",
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
                "demonstrare/static/css/theme.min.css" : "demonstrare/scss/theme.scss"
            }
        }
    },
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
};
