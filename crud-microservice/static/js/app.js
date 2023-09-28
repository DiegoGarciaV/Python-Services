let app = angular.module("usersCrud", []);

app.controller("usersCrudController", function ($scope) {

    const view = $scope;

    view.users = [];

    view.filterUser = 0;

    view.newUser = {

        nombre: "",
        edad: 0,
        locacion: ""
    }

    view.updUserId = 0;

    view.updUser = {

        nombre: "",
        edad: 0,
        locacion: ""
    }

    view.delUser = 0;

    let showInterval = 0;


    view.showUsers = () => {
        $.ajax({
            url: "api/h2/users/",
            method: "GET",
            dataType: "json",
            contentType:    "application/json",   
            success:        (result)  => {
                view.users = result;
                view.$apply();
            }
        });
    }

    view.showUserById = () => {

        clearInterval(showInterval);
        $.ajax({
            url: `api/h2/users/${view.filterUser}` ,
            method: "GET",
            dataType: "json",
            contentType:    "application/json",   
            success:        (result)  => {
                view.users = [result];
                view.$apply();
            }
        });
    }

    view.addUser = () => {
        $.ajax({
            url: "api/h2/users/",
            method: "POST",
            dataType: "json",
            contentType: "application/json",   
            data: JSON.stringify(view.newUser),
            success:        (result)  => {
                
            }
        });
    }

    view.updateUser = () => {
        $.ajax({
            url: `api/h2/users/${view.updUserId}`,
            method: "PUT",
            dataType: "json",
            contentType: "application/json",   
            data: JSON.stringify(view.updUser),
            success:        (result)  => {
                
            }
        });
    }

    view.deleteUser = () => {
        $.ajax({
            url: `api/h2/users/${view.delUser}`,
            method: "DELETE",
            dataType: "json",
            contentType: "application/json",
            success:        (result)  => {
                
              
            }
        });
    }

    view.setCurrentUserData = () => {

        $.ajax({
            url: `api/h2/users/${view.updUserId}` ,
            method: "GET",
            dataType: "json",
            contentType:    "application/json",   
            success:        (result)  => {
                view.updUser = result;
                view.$apply();
            }
        });
    }

    view.showInterval = 0;
    view.startShowing = () =>
    {
        view.showUsers();
        showInterval = setInterval(view.showUsers,1000);
    }

    view.startShowing();
    
    
    

});