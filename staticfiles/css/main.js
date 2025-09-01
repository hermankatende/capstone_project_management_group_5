document.addEventListener('DOMContentLoaded', () => {
  // simple UX: auto-hide flash messages if exist
  const flash = document.querySelector('.flash');
  if (flash) setTimeout(() => flash.remove(), 3500);
});
