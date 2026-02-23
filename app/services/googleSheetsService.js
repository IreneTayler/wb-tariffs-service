const { google } = require('googleapis');

// Update Google Sheets with the tariff data
const updateGoogleSheets = async (tariffs) => {
  const auth = new google.auth.GoogleAuth({
    keyFile: 'path/to/your-service-account.json',  // Replace with the path to your service account JSON file
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });

  const client = await auth.getClient();
  const sheet = google.sheets({ version: 'v4', auth: client });

  const range = 'Sheet1!A1';  // The range where data should be inserted
  const values = tariffs.map(tariff => [tariff.tariff_name, tariff.price]);

  const request = {
    spreadsheetId: 'your_spreadsheet_id',  // Replace with your Google Sheets ID
    range: range,
    valueInputOption: 'RAW',
    resource: {
      values,
    },
  };

  await sheet.spreadsheets.values.update(request);
  console.log('Google Sheets updated');
};

module.exports = { updateGoogleSheets };