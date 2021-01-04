function check_input(ele) {
    // input.addEventListener('change', function () {
        if (ele.checked) {
            // do this
            btn('/led/on',ele)
            console.log('Checked');
        } else {
            // do that
            btn('/led/off',ele)
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
    if (res=="ON") {
        ele.checked=true;
    }
    if (res=="OFF") {
        ele.checked=false;
    }
    if (res=="invalid device") {
        console.log('device not found!')
        ele.checked=false;
    }
}