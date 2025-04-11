function register() {
    
    // ================================================================
    // Get user email
    const client_email = document.getElementById("email").value || "none";
    const client_password = document.getElementById("password").value || "none";
    const client_name = document.getElementById("name").value || "none";
    const client_surname = document.getElementById("surname").value || "none";
    
    // ================================================================
    // Send data to py
    $.ajax({
        url: "/create_account",
        type: "POST",
        data: {
            email: client_email,
            password: client_password,
            name: client_name,
            surname: client_surname,
        },
        dataType: "json",
        success: function() {
            window.location.href = "/"
        }
    })
}
