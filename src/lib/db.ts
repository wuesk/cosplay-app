import { Pool } from 'postgres-pool';
import { env } from '$env/dynamic/private';

const pool = new Pool({
  connectionString: env.DATABASE_URL,
});

export async function query(text: string, params?: any[]) {
  const client = await pool.connect();
  try {
    const result = await client.query(text, params);
    return result;
  } finally {
    client.release();
  }
}