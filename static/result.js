const hyper =document.getElementById("hyper").getAttribute("placeholder");
console.log(hyper)

window.onload = (event) => {
    console.log('page is fully loaded');
    if(hyper === "Yes"){
        document.getElementById("hyper1").classList.add('red-bg');
        
    }
};