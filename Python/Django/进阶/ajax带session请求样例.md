##ajax带session请求样例

    $.ajax({
    type: "GET",
    url: "http://example.com/",
    xhrFields: {withCredentials: true},
    success: function (data) {
        alert(JSON.stringify(data));
        }
    });