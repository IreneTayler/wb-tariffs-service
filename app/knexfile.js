module.exports = {
  client: 'pg',
  connection: {
    host: process.env.DB_HOST || 'db',
    user: process.env.DB_USER || 'postgres',
    password: process.env.DB_PASSWORD || 'password',
    database: process.env.DB_NAME || 'tariffs_db',
  },
};