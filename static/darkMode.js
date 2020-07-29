/*Created by Kayla L. Patterson on 07/28/20
Description: Creates a dark mode feature when toggle button is
clicked on. Used DarkMode.js library to implement this feature.*/

const options = {
  bottom: '64px', // default: '32px'
  left: 'unset', // default: '32px'
  right: '32px', // default: 'unset'
  time: '0.3s', // default: '0.3s'
  mixColor: '#fff', // default: '#fff'
  backgroundColor: '#fff',  // default: '#fff'
  buttonColorDark: '#100f2c',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  saveInCookies: false, // default: true,
  label: '', // default: ''
  autoMatchOsTheme: true // default: true
}

const darkmode =  new Darkmode();

// When toggle switch is clicked on
const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
toggleSwitch.addEventListener('change', switchTheme, false);

function switchTheme(e) {
    //Dark Mode
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        darkmode.toggle();
        console.log(darkmode.isActivated()) // will return true
        localStorage.setItem('theme', 'dark'); //stores dark mode in memory
    }
    //Light Mode
    else {
        document.documentElement.setAttribute('data-theme', 'light');
        darkmode.toggle();
        console.log(!darkmode.isActivated()) // will return false
        localStorage.setItem('theme', 'light'); //stores light mode in memory
    }
}
