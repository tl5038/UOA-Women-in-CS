function ShowAndHide() {
    var searchArea = document.getElementById('searchArea');
    if (searchArea.style.display == 'none') {
        $("#searchArea").slideDown("slow");
    } else {
        $("#searchArea").slideUp("slow");
    }
}

function checkShow() {
    var searchArea = document.getElementById('searchArea');
    if (searchArea.style.display == 'none') {
        $("#searchArea").slideDown("slow");
    }
}