function showReplies(id) {
    var replyArea = document.getElementById(id);
    // let firstChild = replyArea.firstChild;
    // replyArea.classList.remove("show")
    now = replyArea.style.visibility;
    if (now == "visible") {
        replyArea.style.visibility = 'hidden';
    } else {
        replyArea.style.visibility = 'visible'
    }
}