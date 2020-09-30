// // setting Footer with dynamic date
const footer = document.querySelector('#footer');
const year = new Date().getFullYear();
footer.innerHTML = `Copyright &copy; ${year} All Rights Reserved`;