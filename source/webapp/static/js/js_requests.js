function tokenAdd() {
    $.ajax({
        url: 'http://localhost:8000/api/v2/login/',
        method: 'post',
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){localStorage.setItem('apiToken', response.token);},
        error: function(response, status){console.log(response);}
});}


function jqueryParseData(response, status) {
    console.log(response);
    console.log(status);
}

function taskProjectParseData(response, status) {
    console.log(response.tasks);
    console.log(status);
}


function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');
}

function jqueryLoadIndex() {
    $.ajax({
        url: "http://localhost:8000/api/v2/Project/",
        method: 'GET',
        success: jqueryParseData,
        error: jqueryAjaxError
    });
}


function jqueryProjectTask() {
    $.ajax({
        url: "http://localhost:8000/api/v2/Task/",
        method: 'GET',
        success: jqueryParseData,
        error: jqueryAjaxError
    });
}

function taskProject() {
    $.ajax({
        url: "http://localhost:8000/api/v2/Project/1",
        method: 'GET',
        success: taskProjectParseData,
        error: jqueryAjaxError
    });
}


function taskAddProject() {
    $.ajax({
        url: "http://localhost:8000/api/v2/Task/",
        method: 'POST',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        data: JSON.stringify({summary: 'test', description: 'test_desc', status: 1, type: 1, project: 1}),
        dataType: 'json',
        contentType: 'application/json',
        success: taskProjectParseData,
        error: jqueryAjaxError
    });
}




function taskDeleteProject() {
    $.ajax({
        url: "http://localhost:8000/api/v2/Task/14",
        method: 'DELETE',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        dataType: 'json',
        contentType: 'application/json',
        success: jqueryParseData,
        error: jqueryAjaxError
    });
}

$(document).ready(function() {
    jqueryLoadIndex();
    jqueryProjectTask();
    taskProject();
    tokenAdd();
    taskAddProject();
    taskDeleteProject();
});






