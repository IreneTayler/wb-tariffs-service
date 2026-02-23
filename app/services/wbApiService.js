const axios = require('axios');
const knex = require('knex')(require('../knexfile'));

// Fetch tariff data from Wildberries API
const fetchTariffs = async () => {
  try {
    const response = await axios.get('https://common-api.wildberries.ru/api/v1/tariffs/box');
    const tariffs = response.data.tariffs;

    // Insert tariffs data into the PostgreSQL database
    await knex('tariffs').insert(tariffs);
    console.log('Tariffs updated successfully');
  } catch (error) {
    console.error('Error fetching tariffs:', error);
  }
};

module.exports = { fetchTariffs };