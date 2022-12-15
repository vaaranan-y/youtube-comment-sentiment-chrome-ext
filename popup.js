var serverhost = "http://127.0.0.1:8000";

const fetchData = async (rawComment) => {
  let comment = rawComment.replace(" ", "-");
  var url =
    serverhost + "/sentiment-analyzer/get-text-sentiment/" + "I-am-excited";
  const options = {
    method: "GET",
  };
  const res = {};
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
};

let submitButton = document.getElementById("subjectSubmit");

const submitText = () => {
  let comment = document.getElementById("subjectText").value;
  console.log(comment);

  if (comment) {
    fetchData(comment).then((response) => {
      console.log(response);
    });
  }
};

if (submitButton) {
  console.log("the submit button exists");
  submitButton.addEventListener("click", submitText);
}
