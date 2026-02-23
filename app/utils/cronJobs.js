const { fetchTariffs } = require('../services/wbApiService');
const { updateGoogleSheets } = require('../services/googleSheetsService');

// Run tariff fetching every 24 hours
setInterval(fetchTariffs, 24 * 60 * 60 * 1000); // every 24 hours

// Run Google Sheets update every 24 hours
setInterval(updateGoogleSheets, 24 * 60 * 60 * 1000); // every 24 hours