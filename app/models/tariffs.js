const axios = require('axios');
const knex = require('knex')(require('../knexfile'));

// Fetch tariffs from the Wildberries API
const fetchTariffs = async () => {
  try {
    // Wildberries API request
    const response = await axios.get('https://common-api.wildberries.ru/api/v1/tariffs/box');
    const tariffs = response.data.tariffs;

    // nserting data into a database
    await knex('tariffs').insert(tariffs);
    console.log('Tariffs fetched and inserted successfully');
  } catch (error) {
    console.error('Error fetching tariffs:', error);
    throw new Error('Error fetching tariffs');  // Throws an error message so that the caller can catch the error.
  }
};

module.exports = { fetchTariffs };