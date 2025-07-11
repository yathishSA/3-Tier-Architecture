
document.addEventListener("DOMContentLoaded", async () => {
    const userName = localStorage.getItem("userName");
    if (userName) {
        document.getElementById("welcome-message").textContent = `Welcome, ${userName}!`;
    }

    const response = await fetch("http://127.0.0.1:5000/messi");
    const data = await response.json();

    if (response.ok) {
        document.getElementById("messi-image").src = data.image_url;
    }
});
