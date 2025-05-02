// let isOriginal=true;
// function theme(){
//     if (isOriginal) {
//         document.body.style.backgroundColor="black";
//         document.body.style.color="white";
//         let border=document.getElementById('navbar');
//         border.style.borderColor="white";
//         let con =document.getElementById('theme');
//         con.innerHTML='Light';
//         let search=document.getElementById('search');
//         search.style.backgroundColor='black';
//         search.style.color='white';
//         search.style.borderColor='white';
//         let grid=document.getElementById('g');
//         grid.style.borderColor='white';

//     }
//     else{
//         document.body.style.backgroundColor="white";
//         document.body.style.color="black";
//         let border=document.getElementById('navbar');
//         border.style.borderColor="black";
//         let con =document.getElementById('theme');
//         con.innerHTML='Dark';
//         let search=document.getElementById('search');
//         search.style.backgroundColor='white';
//         search.style.color='black';
//         search.style.borderColor='black';
//         let grid=document.getElementById('g');
//         grid.style.borderColor='black';
//     }
//     isOriginal = !isOriginal;
// }
function showPage(pageId) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.style.display = 'none';
    });

    // Show the selected page
    document.getElementById(pageId).style.display = 'block';
}
// Show home page by default
document.addEventListener("DOMContentLoaded", () => {
    showPage('home');
});


function input(){
    let search = document.getElementById("search");
    let v=search.value.trim();
    if (v==="") {
        let alert=document.getElementById('alert');
        alert.innerText="Enter Something";
        alert.style.color="red";
        alert.style.fontSize="20px";
        alert.style.fontWeight="bold";
        alert.style.textAlign='center'
    } else {
        showproduct()
        let alert=document.getElementById('alert');
        alert.innerText="";
    }

}
let dataCache = []; // Store JSON data
let currentIndex = 0; // Track loaded items
const itemsPerClick = 8;

// Define a whitelist of allowed JSON file names (without the .json extension)
const allowedFiles = ["bottle", "bag", "shoe", "four"]; // Add your allowed file names here

async function fetchJsonFile(fileName) {
    try {
        let response = await fetch(`/static/webtechstyles/Data/${fileName}.json`);
        if (!response.ok) throw new Error("File not found");

        dataCache = await response.json();
        console.log(`Loaded data for ${fileName}`, dataCache);

        currentIndex = 0;
        document.getElementById("main").innerHTML = "";
        loadmore();
    } catch (error) {
        console.error(`Error fetching data for ${fileName}:`, error);
        alert("File not found or not allowed!");
    }
}



function loadmore() {
    let container = document.getElementById("main");
    if (currentIndex >= dataCache.length) {
        document.getElementById('load').innerText="Nothing More";
        return;
    }
    else{
        document.getElementById('load').innerText="Load More";
    for (let i = 0; i < itemsPerClick && currentIndex < dataCache.length; i++, currentIndex++) {
        let item = dataCache[currentIndex];
        let newele = document.createElement("div");
        newele.classList.add("grid");
        newele.innerHTML = `
            <img src="${item.img}" alt="Image">
            <button id="c" onclick="showPage('compareprod')">Compare</button>
        `;
        container.appendChild(newele);
    }}
}



function showproduct() {
    let searchValue = document.getElementById("search").value.toLowerCase();
    document.getElementById("rec").innerHTML = `Showing results for "${searchValue}"`;

    // Find the first matching file name in the input
    let foundFile = allowedFiles.find(file => searchValue.includes(file));

    if (foundFile) {
        fetchJsonFile(foundFile); // Fetch the corresponding JSON file
        document.getElementById('load').style.display = 'block';
    } else {
        document.getElementById("rec").innerHTML = `No Results`;
        document.getElementById('load').innerText = "";
        document.getElementById('main').innerHTML = "";
        document.getElementById('load').style.display = 'block';
    }
}

