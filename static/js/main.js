// document.addEventListener("DOMContentLoaded", function () {
//     var pins = document.getElementsByTagName("input");
//     var pinids = [].map.call(pins, function (elem) {
//         return elem.id;
//     });
//     for (i = 0; i < pinids.length; i++) {
//         btn("/led/sync", document.getElementById(pinids[i]));
//     }
//     setInterval(function () {
//         for (i = 0; i < pinids.length; i++) {
//             btn("/led/sync", document.getElementById(pinids[i]));
//         }
//     }, 3000);
// });

function check_input(ele) {
    data = {node:ele.parentNode.parentNode.id , pin:ele.id , status:""};
    if (ele.checked) {
        data["status"]="on";
        send_req("POST", data,ele);
    } else {
        data["status"]="off"
        send_req("POST", data,ele);
        console.log('Not checked');
    }
}

function send_req(method,data="",ele) {
    if (method == "POST") {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                postresponse = this.responseText;
                changebtn(postresponse,ele);
            }
        };
        xhttp.open("POST", "/api/v1/update", true);
        xhttp.setRequestHeader('Content-Type', 'application/json');
        xhttp.send(JSON.stringify(data));
    }
    if (method == "GET") {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                getresponse=this.responseText;
                changebtn(getresponse,ele)
            }
        };
        xhttp.open("GET", "/api/v1/update", true);
        xhttp.send();
    }
}

function changebtn(res, ele) {
    if (res == "on") {
        ele.checked = true;
    }
    if (res == "off") {
        ele.checked = false;
    }
    if (res == "invalid device") {
        console.log('device not found!')
        ele.checked = false;
    }
}