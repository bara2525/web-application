// let menu;
// let toggle;
//
//
// function initializeMenu() {
//     toggle = document.getElementById("menu-toggle");
//     menu = document.getElementById("nav-list");
//
//     toggle.addEventListener('click', toggleMenu);
//     menu.addEventListener('click', toggleMenu);
//
//
// }
//
// function toggleMenu() {
//     const isVisible = menu.classList.contains("expanded");
//
//     if (isVisible) {
//         menu.classList.remove('expanded');
//     } else {
//         menu.classList.add('expanded');
//     }
// }
//
//
//
//
// // Get the container element
// function abc(){
//     var btnContainer = document.getElementsByClassName('navbar');
//     console.log(btnContainer);
//
//
//     var number = document.getElementById('contact');
//     console.log(number);
//
//
// }
//



// Get all buttons with class="btn" inside the container



//Loop through the buttons and add the active class to the current/clicked button
//
// for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function() {
//         var current = document.getElementsByClassName("active");
//         if (current.length > 0) {
//             current[0].className = current[0].className.replace(" active", "");
//         }
//
//         this.className += " active";
//
//     });
// }

let login = false

function logged_in(){
    return login;

}

function change_login(){
    login = login !== true;
    //alert(login)
    }

function visible(){
    x = document.getElementById("log");
    if (logged_in()) {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
    //alert(login)
}




function foo() {
    alert("Submit button clicked!");
    return true;
}


let x

function myFunction() {

    x = document.getElementById("form_product");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

// main
document.addEventListener("DOMContentLoaded", () => {

    //visible();

    // abc();
    // initializeMenu();
    //
    // initializeSlideshow();
    // moveSlide(1);


});

function get_dynamic_url() {
    url = "one_category.html";
    $("#addBtn").attr("href", url);
    return true;
}

function showDatabase(database) {

    let text = "";
    for (let i = 0; i < database.length; i++) {
        text += database[i] + "<br>";
    }


}