exports.up = function(knex) {
  return knex.schema.createTable('tariffs', table => {
    table.increments('id').primary();  // id column, primary key
    table.string('tariff_name');        // ariff_name column
    table.decimal('price', 10, 2);     // Set the price column to DECIMAL(10, 2) (up to 2 decimal places)
    table.string('description', 255);  // description column, set to VARCHAR(255)
    table.timestamps(true, true);      // Automatically generate created_at and updated_at timestamps
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists('tariffs');  // Delete if table exists
};