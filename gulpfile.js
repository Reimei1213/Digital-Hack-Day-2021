const gulp = require("gulp");
const connect = require("gulp-connect")

gulp.task("connect", function(done) {
    connect.server({
        root: "./",
        livereload: true,
        host: "0.0.0.0",
        port: 3000
    });
    done();
});

gulp.task("html", function(done) {
    gulp.src("./*.html")
        .pipe(connect.reload());
    done();
});

gulp.task("watch", function(done) {
    gulp.watch("./*.html", gulp.task("html"));
});

gulp.task("default", gulp.series("connect", "watch", function(done) {
    console.log("run default tasks");
    done();
}));