window.onload = function() {
  let inputs = document.querySelectorAll('.inputLabel input, .inputLabel textarea');
  for (let input of inputs) {
    input.setAttribute('value', input.value)
  }
};