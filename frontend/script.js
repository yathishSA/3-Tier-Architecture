
document.getElementById("login-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email }),
    });

    if (response.ok) {
        localStorage.setItem("userName", name);
        window.location.href = "welcome.html";
    } else {
        alert("Login failed");
    }
});
