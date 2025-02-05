document
  .getElementById("contact-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const submitButton = this.querySelector("button[type=sumbit]");
    submitButton.classList.add("loading");
    const formData = new FormData(this);
    fetch("/send_email", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        console.log("mensaje enviado");
        this.reset();
        submitButton.classList.remove("loading");
      })
      .catch((error) => {
        console.log("error", error);
        submitButton.classList.remove("loading");
      });
  });
