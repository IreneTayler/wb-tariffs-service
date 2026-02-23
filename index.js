const express = require('express');
const appRoutes = require('./app/index');  // Import routing settings from app/index.js
const app = express();
const port = process.env.PORT || 3000;

// Added handling for root path '/'
app.get('/', (req, res) => {
  res.send('Welcome to WB Tariffs Service!');  // Basic message
});

// Using the router in the app folder
app.use('/', appRoutes);  // Use the router set in app/index.js

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});