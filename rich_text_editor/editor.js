const editor = document.getElementById("editor");
const toolbarButtons = document.querySelectorAll("[data-command]");
const fontFamilySelect = document.getElementById("font-family");
const fontSizeSelect = document.getElementById("font-size");
const textColorInput = document.getElementById("text-color");
const highlightInput = document.getElementById("highlight-color");
const insertLinkButton = document.getElementById("insert-link");
const insertImageButton = document.getElementById("insert-image");
const insertTableButton = document.getElementById("insert-table");
const downloadButton = document.getElementById("download-html");
const clearStorageButton = document.getElementById("clear-storage");

const STORAGE_KEY = "rich-text-editor-content";

const loadSavedContent = () => {
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    editor.innerHTML = saved;
  }
};

const saveContent = () => {
  localStorage.setItem(STORAGE_KEY, editor.innerHTML);
};

const exec = (command, value = null) => {
  document.execCommand(command, false, value);
  editor.focus();
};

toolbarButtons.forEach((button) => {
  button.addEventListener("click", () => {
    exec(button.dataset.command);
  });
});

fontFamilySelect.addEventListener("change", (event) => {
  exec("fontName", event.target.value);
});

fontSizeSelect.addEventListener("change", (event) => {
  exec("fontSize", event.target.value);
});

textColorInput.addEventListener("input", (event) => {
  exec("foreColor", event.target.value);
});

highlightInput.addEventListener("input", (event) => {
  exec("hiliteColor", event.target.value);
});

insertLinkButton.addEventListener("click", () => {
  const url = prompt("Enter the URL:");
  if (url) {
    exec("createLink", url);
  }
});

insertImageButton.addEventListener("click", () => {
  const url = prompt("Enter the image URL:");
  if (url) {
    exec("insertImage", url);
  }
});

insertTableButton.addEventListener("click", () => {
  const rows = Number.parseInt(prompt("Number of rows?", "2"), 10);
  const columns = Number.parseInt(prompt("Number of columns?", "2"), 10);

  if (!Number.isNaN(rows) && !Number.isNaN(columns) && rows > 0 && columns > 0) {
    let tableHtml = "<table><tbody>";
    for (let row = 0; row < rows; row += 1) {
      tableHtml += "<tr>";
      for (let col = 0; col < columns; col += 1) {
        tableHtml += "<td>New cell</td>";
      }
      tableHtml += "</tr>";
    }
    tableHtml += "</tbody></table>";
    exec("insertHTML", tableHtml);
  }
});

const downloadHtml = () => {
  const htmlContent = editor.innerHTML;
  const blob = new Blob([htmlContent], { type: "text/html" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = "rich-text-content.html";
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  URL.revokeObjectURL(url);
};

const clearAutosave = () => {
  localStorage.removeItem(STORAGE_KEY);
};

editor.addEventListener("input", saveContent);
window.addEventListener("load", loadSavedContent);

downloadButton.addEventListener("click", downloadHtml);
clearStorageButton.addEventListener("click", clearAutosave);
