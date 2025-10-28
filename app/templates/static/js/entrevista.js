document.addEventListener("DOMContentLoaded", () => {
  const steps = Array.from(document.querySelectorAll(".form-step"));
  const nextBtns = Array.from(document.querySelectorAll(".next-step"));
  const prevBtns = Array.from(document.querySelectorAll(".prev-step"));
  const circles = Array.from(document.querySelectorAll(".step-circle"));
  let current = 0;

  if (!steps.length) return;

  function updateUI() {
    steps.forEach((s, i) => s.classList.toggle("form-step-active", i === current));
    circles.forEach((c, i) => c.classList.toggle("active", i <= current));
  }

  nextBtns.forEach(btn => btn.addEventListener("click", (e) => {
    e.preventDefault();
    if (current < steps.length - 1) {
      current++;
      updateUI();
    }
  }));

  prevBtns.forEach(btn => btn.addEventListener("click", (e) => {
    e.preventDefault();
    if (current > 0) {
      current--;
      updateUI();
    }
  }));

  const modal = document.getElementById("modalEntrevista");
  if (modal) {
    modal.addEventListener("show.bs.modal", () => {
      current = 0;
      updateUI();
    });
  }

  updateUI();
});
