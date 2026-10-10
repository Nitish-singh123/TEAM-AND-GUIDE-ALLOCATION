document.querySelectorAll("[data-nav-toggle]").forEach((button) => {
  button.addEventListener("click", () => {
    const navigation = document.getElementById(button.dataset.navToggle);
    if (!navigation) {
      return;
    }

    const isExpanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!isExpanded));
    navigation.classList.toggle("show", !isExpanded);
  });
});
