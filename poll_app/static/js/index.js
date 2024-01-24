let questionCounter = 1;
let optionCounter = 1;

function showForm() {
  document.getElementById("formContainer").style.display = "block";
}

function generateOption() {
  const optionsContainer = document.getElementById("optionsContainer");

  const optionLabel = document.createElement("div");
  optionLabel.className = "mb-3";
  optionLabel.innerHTML = `
      <label for="option_${optionCounter}" class="form-label">Enter Option ${optionCounter}:</label>
      <input type="text" class="form-control" id="option_${optionCounter}" required>
    `;
  optionsContainer.appendChild(optionLabel);

  optionCounter++;
}

function saveQuestionOptions() {
  const question = document.getElementById("question").value;
  const options = Array.from(
    document.querySelectorAll('[id^="option_"]'),
    (option) => option.value
  );

  const questionData = {
    question: question,
    options: options,
  };

  const savedQuestions =
    JSON.parse(localStorage.getItem("savedQuestions")) || [];

  savedQuestions.push(questionData);

  localStorage.setItem("savedQuestions", JSON.stringify(savedQuestions));

  displaySavedQuestions();

  clearForm();
}

function displaySavedQuestions() {
  const savedQuestionsContainer = document.getElementById("savedQuestions");
  savedQuestionsContainer.innerHTML = "";

  const savedQuestions =
    JSON.parse(localStorage.getItem("savedQuestions")) || [];

  savedQuestions.forEach((questionData, index) => {
    const savedQuestionElement = document.createElement("div");
    savedQuestionElement.innerHTML = `
      <div class="mb-3">
        <label class="form-label">${questionData.question}</label>
        ${questionData.options
          .map(
            (option, optionIndex) => `
          <div class="form-check">
            <input type="radio" id="choose_${index + 1}_${
              optionIndex + 1
            }" class="form-check-input" disabled>
            <label class="form-check-label">${option}</label>
          </div>
        `
          )
          .join("")}
          <button
            type="button"
            class="btn btn-primary"
            onclick="saveRecord(${index})" // Pass the index to identify which question to save
          >
            Save Record
          </button>
      </div>
    `;
    savedQuestionsContainer.appendChild(savedQuestionElement);
  });
}

function saveRecord(index) {
  // Handle saving the record for the specific question (use the index)
  // For demonstration purposes, you can just log the question data
  const savedQuestions =
    JSON.parse(localStorage.getItem("savedQuestions")) || [];

  const questionData = savedQuestions;
  console.log("Saving Record:", questionData);
}

function clearForm() {
  document.getElementById("pollForm").reset();
  document.getElementById("optionsContainer").innerHTML = "";
  document.getElementById("formContainer").style.display = "none";
  optionCounter = 1;
}

displaySavedQuestions();
