function topFunction(){
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function loading(){
    document.getElementById("form").style.setProperty("display", "none", "important");
    document.getElementById("loading").style.setProperty("display", "block", "important");
}