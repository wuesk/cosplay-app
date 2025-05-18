import { json } from '@sveltejs/kit';
import { query } from '$lib/db';

export async function GET() {
  try {
    const result = await query('SELECT NOW()');
    return json({ timestamp: result.rows[0].now });
  } catch (error: any) {
    return json({ error: error.message }, { status: 500 });
  }
}