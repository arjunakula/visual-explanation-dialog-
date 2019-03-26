var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }

  if (n == 4 || n == 5) {
    document.getElementById("questionImg").src = "static/img/question2.png";
  } else if (n == 8) {
    document.getElementById("questionImg").src = "static/img/question3.png";
  } else {
    document.getElementById("questionImg").src = "static/img/question1.png";
  }
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    processInputs();
    window.location.replace("evaluator_results.html");
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function processInputs() {
  answers_dict = {};
  answers_dict[1] = getRadioVal("q1");
  answers_dict[2] = getCheckboxVals("q2");
  answers_dict[3] = getCheckboxVals("q3");
  answers_dict[4] = getCheckboxVals("q4");
  answers_dict[5] = getRadioVal("q5");
  answers_dict[6] = getCheckboxVals("q6");
  answers_dict[7] = getCheckboxVals("q7");
  answers_dict[8] = getRadioVal("q8");

  var explainer_type = getRadioVal("q0");
  switch (explainer_type) {
    case "no explanation":
      sessionStorage.setItem("wo_explanation_answers", JSON.stringify(answers_dict));
      break;
    case "attention maps":
      sessionStorage.setItem("attention_maps_answers", JSON.stringify(answers_dict));
      break;
    case "x-tom":
      sessionStorage.setItem("x-tom_answers", JSON.stringify(answers_dict));
      break;
    default:
      break;
  }
  
}

function getCheckboxVals(name) {
  var vals = [];
  var boxes = document.getElementsByName(name);
  for (var i=0, len=boxes.length; i < len; i++) {
    if (boxes[i].checked) {
      vals.push(boxes[i].value);
    }
  }
  return vals;
}

function getRadioVal(name) {
  var radios = document.getElementsByName(name);
  for (var i=0, len=radios.length; i < len; i++) {
    if (radios[i].checked) {
      return radios[i].value;
    }
  }
  return null;
}
