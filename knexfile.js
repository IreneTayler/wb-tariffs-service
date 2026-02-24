module.exports = {
  client: 'postgresql',
  connection: {
    host: 'localhost',
    user: 'postgres',
    password: '12345678', 
    database: 'tariffs_db',
    port: 5432,
  },
  migrations: {
    directory: './app/migrations', 
  },
};
// module.exports = {
//   client: 'pg',  // use PostgreSQL 
//   connection: {
//     host: process.env.DB_HOST || 'db',  // Using the 'db' container in a Docker environment
//     user: process.env.DB_USER || 'postgres',  // PostgreSQL username
//     password: process.env.DB_PASSWORD || 'password',  // PostgreSQL password
//     database: process.env.DB_NAME || 'tariffs_db',  // Database name
//     port: process.env.DB_PORT || 5432,  // PostgreSQL port
//   },
//   migrations: {
//     tableName: 'knex_migrations',  // Migration table name
//     directory: './app/migrations',  // Folder where the migration files will be located
//   },
//   seeds: {
//     directory: './app/seeds',  // Folder where seed data will be located
//   },
// };
