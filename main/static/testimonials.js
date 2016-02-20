function fade () { $('.jumbotron > ul > li').each(function (i, elem) {
    window.setTimeout(function() {
        $(elem).fadeIn(2000);
    }, i * 5000);
    window.setTimeout(function() {
        $(elem).fadeOut(2000);
    }, i * 5000);
})}
    fade();
    setInterval(fade, 40000);