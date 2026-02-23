exports.up = function(knex) {
  return knex.schema.createTable('tariffs', table => {
    table.increments('id').primary();
    table.string('tariff_name');
    table.float('price');
    table.timestamps(true, true); // created_at, updated_at
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists('tariffs');
};