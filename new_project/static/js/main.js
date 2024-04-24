// console.log('Name', 'Shahidur');
// Search Hint AJAX
function myFun(keyword) {
    console.log('keyword', keyword);
    if (keyword.length == 0) {
        document.getElementById('txtHint').innerHTML = '';
        return;
    } else {
        const xmlhttp = new XMLHttpRequest();
        xmlhttp.onload = function() {
        document.getElementById('txtHint').innerHTML = this.responseText;
    }
    xmlhttp.open('GET', 'result/'+ keyword);
    xmlhttp.send();
    }
}

// Background Color Change JAVA

function newColor() {
    document.getElementById('color').style.backgroundColor =
    'blue';
}

function prevColor() {
    document.getElementById('color').style.backgroundColor =
    'grey';
}