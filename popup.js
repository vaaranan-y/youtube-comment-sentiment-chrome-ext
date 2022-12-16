var serverhost = "http://127.0.0.1:8000";


const fetchVideoData = async (videoId) => {
  var url = serverhost + "/sentiment-analyzer/get-video-sentiment/" + videoId;
  console.log(url);
  const options = {
    method: "GET",
  };
  const res = {};
  let response = await fetch(url, options);
  let data = await response.json();
  return data;
};

// const fetchTextData = async (rawComment) => {
//   let comment = rawComment.replace(" ", "-");
//   var url =
//     serverhost + "/sentiment-analyzer/get-text-sentiment/" + "I-am-excited";
//   const options = {
//     method: "GET",
//   };
//   const res = {};
//   fetch(url)
//     .then((response) => response.json())
//     .then((data) => {
//       return data;
//     });
// };

let submitButton = document.getElementById("subjectSubmit");

// const submitText = () => {
//   let comment = document.getElementById("subjectText").value;
//   console.log(comment);

//   if (comment) {
//     fetchTextData(comment).then((response) => {
//       console.log(response);
//     });
//   }
// };

const getVideoSentiment = async () => {
  let videoId = document.getElementById("subjectText").value;
  console.log(videoId);

  if (videoId) {
    let response = await fetchVideoData(videoId);
    console.log(JSON.stringify(response));
  }
};

if (submitButton) {
  console.log("the submit button exists");
  submitButton.addEventListener("click", getVideoSentiment);
}
