const navToggle = document.querySelector("[data-nav-toggle]");
const navMenu = document.querySelector("[data-nav-menu]");
const modal = document.getElementById("download-modal");
const modalDescription = document.getElementById("modal-description");
const modalDownloadLink = document.getElementById("modal-download-link");
const downloadButtons = document.querySelectorAll("[data-download-button]");
const closeModalButtons = document.querySelectorAll("[data-close-modal]");

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("is-open");
  });
}

const openModal = (programTitle, downloadUrl) => {
  if (!modal || !modalDescription || !modalDownloadLink) {
    return;
  }

  modalDescription.textContent = `Ви збираєтесь завантажити ${programTitle}. Натисніть кнопку нижче, щоб продовжити.`;
  modalDownloadLink.href = downloadUrl;
  modal.classList.add("is-open");
  modal.setAttribute("aria-hidden", "false");
  document.body.classList.add("modal-open");
};

const closeModal = () => {
  if (!modal) {
    return;
  }

  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");
};

downloadButtons.forEach((button) => {
  button.addEventListener("click", () => {
    openModal(button.dataset.programTitle, button.dataset.downloadUrl);
  });
});

closeModalButtons.forEach((button) => {
  button.addEventListener("click", closeModal);
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    closeModal();
  }
});
