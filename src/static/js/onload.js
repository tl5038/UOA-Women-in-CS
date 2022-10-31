window.onload = (event) => {
    const selected = new URLSearchParams(window.location.search).get("selected");
    if (selected == null) {
        document.getElementById('select').value = "everything";
    } else {
        document.getElementById('select').value = selected;
        var searchArea = document.getElementById('searchArea');
        searchArea.style.display = 'block';
    }
};