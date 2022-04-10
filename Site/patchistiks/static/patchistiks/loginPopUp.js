let popup = document.querySelector(".loginButton");
let openPopup = document.querySelector(".openButton");
let closePopup = document.querySelector(".closeButton");

openPopup.addEventListener("click", () => {
    popup.showModal();
});

closePopup.addEventListener('click', () =>{
    popup.close();
})