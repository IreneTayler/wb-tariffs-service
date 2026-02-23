const knex = require('./knexfile'); // 루트 디렉토리로부터 knexfile.js를 불러옵니다.
const express = require('express');
const { fetchTariffs } = require('./services/wbApiService');
const { updateGoogleSheets } = require('./services/googleSheetsService');

const router = express.Router();

// /fetch-tariffs endpoint: Logic for retrieving data from the Wildberries API.
router.get('/fetch-tariffs', async (req, res) => {
  try {
    await fetchTariffs(); // Retrieving data from API
    res.send('Tariffs fetched successfully!');
  } catch (error) {
    console.error('Error fetching tariffs:', error);
    res.status(500).send('Error fetching tariffs');
  }
});

// /update-google-sheets endpoint: Update Google Sheets from a database.
router.get('/update-google-sheets', async (req, res) => {
  try {
    const tariffs = await knex('tariffs').select(); // Retrieving data from a database
    await updateGoogleSheets(tariffs); // Google Sheets Update
    res.send('Google Sheets updated successfully!');
  } catch (error) {
    console.error('Error updating Google Sheets:', error);
    res.status(500).send('Error updating Google Sheets');
  }
});

module.exports = router;