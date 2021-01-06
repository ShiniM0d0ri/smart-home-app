document.addEventListener("DOMContentLoaded", function() {
    var pins = document.getElementsByTagName("input");
    var pinids = [].map.call(pins, function(elem) {
    return elem.id;  
    });
    for(i=0;i<pinids.length;i++) {
        btn("/led/sync",document.getElementById(pinids[i]));
    }
    setInterval(function(){ 
        for(i=0;i<pinids.length;i++) {
            btn("/led/sync",document.getElementById(pinids[i]));
        }
    }, 3000);
});


function check_input(ele) {
    // input.addEventListener('change', function () {
        if (ele.checked) {
            // do this
            btn('/'+ele.id+'/on',ele);
            console.log('Checked');
        } else {
            // do that
            btn('/'+ele.id+'/off',ele);
            console.log('Not checked');
        }
    // });
}
function btn(req,ele) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', req, true);

    // If specified, responseType must be empty string or "text"
    xhr.responseType = 'text';
    var res=""
    xhr.onload = function () {
        if (xhr.readyState === xhr.DONE) {
            if (xhr.status === 200) {
                res=xhr.response;
                changebtn(res,ele);
            }
        }
    };
    xhr.send(null);
}

function changebtn(res,ele) {
    if (res=="on") {
        ele.checked=true;
    }
    if (res=="off") {
        ele.checked=false;
    }
    if (res=="invalid device") {
        console.log('device not found!')
        ele.checked=false;
    }
}