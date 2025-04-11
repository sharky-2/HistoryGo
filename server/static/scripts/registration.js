function register() {
    
    // ================================================================
    // Get user email
    const client_email = document.getElementById("email").value || "none";
    const client_password = document.getElementById("password").value || "none";
    const client_name = document.getElementById("name").value || "none";
    const client_surname = document.getElementById("surname").value || "none";
    const client_profile_picature = document.getElementById("pfp").value || "none";

    console.log(`Sending Data: ${client_email}, ${client_password}, ${client_name}, ${client_surname}, ${client_profile_picature}`);
    
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
            pfp: client_profile_picature
        },
        dataType: "json",
        success: function(response) {
            if (response.success) {
                window.location.href = "/"
            } else {
                window.location.href = "/registration"
            }
        }
    })
}
