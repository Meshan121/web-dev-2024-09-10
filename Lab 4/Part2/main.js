const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */
const imageFilenames = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg', 'pic5.jpg'];
/* Declaring the alternative text for each image file */
const imageAlts = {
    'pic1.jpg': 'A close-up of an eye',
    'pic2.jpg': 'A desert landscape',
    'pic3.jpg': 'Beautiful flowers',
    'pic4.jpg': 'Ancient Egyptian mummies',
    'pic5.jpg': 'A colorful butterfly',
  };
/* Looping through images */

for (const filename of imageFilenames) {
    const newImage = document.createElement('img'); // Create a new <img> element
    newImage.setAttribute('src', `${filename}`); // Set the src to the correct image path
    newImage.setAttribute('alt', imageAlts[filename]); // Set the alt text using the imageAlts object
    thumbBar.appendChild(newImage); // Append the new <img> to the thumb-bar
  
    // Add a click event listener to update the displayed image
    newImage.addEventListener('click', () => {
      displayedImage.setAttribute('src', `${filename}`); // Update displayed image src
      displayedImage.setAttribute('alt', imageAlts[filename]); // Update displayed image alt
    });
  }  

/* Wiring up the Darken/Lighten button */
btn.addEventListener('click', () => {
    const currentClass = btn.getAttribute('class'); // Get current class of the button
    if (currentClass === 'dark') {
      btn.setAttribute('class', 'light'); // Change button class to "light"
      btn.textContent = 'Lighten'; // Change button text to "Lighten"
      overlay.style.backgroundColor = 'rgb(0 0 0 / 50%)'; // Apply dark overlay
    } else {
      btn.setAttribute('class', 'dark'); // Change button class to "dark"
      btn.textContent = 'Darken'; // Change button text to "Darken"
      overlay.style.backgroundColor = 'rgb(0 0 0 / 0%)'; // Remove overlay
    }
  });