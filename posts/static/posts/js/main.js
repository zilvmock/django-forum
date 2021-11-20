function showReplies(id) {
    var replyArea = document.getElementById(id);
    now = replyArea.style.visibility;
    if (now == "visible") {
        replyArea.style.visibility = 'hidden';
    } else {
        replyArea.style.visibility = 'visible'
    }
}