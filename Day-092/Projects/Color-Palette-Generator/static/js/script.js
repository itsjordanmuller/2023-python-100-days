// Add this to your static/js/script.js file

function copyToClipboard(hex) {
  navigator.clipboard.writeText(hex).then(
    function () {
      alert("Copied " + hex + " to clipboard");
    },
    function (err) {
      console.error("Could not copy text: ", err);
    }
  );
}
