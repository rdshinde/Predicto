var weight = document.querySelector('#weight');
var height = document.querySelector('#height');
var bmi = document.querySelector("#BMI");
var submit = document.querySelector('#submit');

function submitHandler() {
    var heightValue = (parseInt(height.value)) / 100;
    var bmiValue = parseInt(weight.value) / heightValue / heightValue;
    bmi.placeholder = Math.round(bmiValue * 100) / 100;
}
submit.addEventListener("click", submitHandler);