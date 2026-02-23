const express = require('express');
const knex = require('knex')(require('./knexfile'));
const { fetchTariffs } = require('./services/wbApiService');
const { updateGoogleSheets } = require('./services/googleSheetsService');
const cronJobs = require('./utils/cronJobs');

const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('WB Tariffs Service Running');
});

// Manually fetch tariffs from WB API
app.get('/fetch-tariffs', async (req, res) => {
  try {
    await fetchTariffs();
    res.send('Tariffs fetched successfully!');
  } catch (error) {
    res.status(500).send('Error fetching tariffs');
  }
});

// Manually update Google Sheets
app.get('/update-google-sheets', async (req, res) => {
  try {
    const tariffs = await knex('tariffs').select();
    await updateGoogleSheets(tariffs);
    res.send('Google Sheets updated successfully!');
  } catch (error) {
    res.status(500).send('Error updating Google Sheets');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});