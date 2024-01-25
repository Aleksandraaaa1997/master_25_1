
function validateForm(event) {
    console.log("Event:", event);
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var repeatPassword = document.getElementById('repeatPassword').value;

    // Resetujte prethodne poruke o greškama
    document.getElementById('emailError').innerHTML = '';
    document.getElementById('passwordError').innerHTML = '';

    // Provera za svako polje
    var valid = true;

    if (email === '') {
        document.getElementById('emailError').innerHTML = 'Molimo vas da popunite ovo polje.';
        valid = false;
    }

    if (username === '') {
        document.getElementById('usernameError').innerHTML = 'Molimo vas da popunite ovo polje.';
        valid = false;
    }

    if (password === '') {
        document.getElementById('passwordError').innerHTML = 'Molimo vas da popunite ovo polje.';
        valid = false;
    }

    if (repeatPassword === '') {
        document.getElementById('repeatPasswordError').innerHTML = 'Molimo vas da popunite ovo polje.';
        valid = false;
    }

    // Matching passwords
    console.log(password);
    console.log(repeatPassword);
    event.preventDefault();
    if (password !== repeatPassword) {
        document.getElementById('passwordError').innerHTML = 'Šifre se ne podudaraju.';
        valid = false;
    }
    console.log(valid);
    if (valid) {
        // If valid, submit the form
        document.getElementById('registerForm').submit();
    } else {
        // If not valid, prevent default form submission
        event.preventDefault();
    }


    return valid;
}

