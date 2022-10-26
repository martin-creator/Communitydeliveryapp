importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js")

firebase.initializeApp({
    apiKey: "AIzaSyAd44NtKzs-G_4k5zuxNKw2_laWj8cMv9Y",
    authDomain: "quick-parcel-92a1f.web.app",
    projectId: "quick-parcel-92a1f",
    storageBucket: "quick-parcel-92a1f.appspot.com",
    messagingSenderId: "481072622582",
    appId: "1:481072622582:web:8237660a8722fdf79df5d7",
  });

const messaging = firebase.messaging();