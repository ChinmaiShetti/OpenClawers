// lib/api.ts — Typed fetch wrapper
// All API calls go through here. Never use raw fetch() in components.

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'
const AI_URL  = process.env.NEXT_PUBLIC_AI_URL  ?? 'http://localhost:9000'

async function request<T>(base: string, path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${base}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options?.headers },
    ...options,
  })
  if (!res.ok) {
    const err = await res.text()
    throw new Error(`API Error ${res.status}: ${err}`)
  }
  return res.json() as Promise<T>
}

// ── Backend (port 8000) ───────────────────────────────────────
export const api = {
  getEntries: (module: string, params?: { limit?: number; offset?: number; user_id?: string }) => {
    const qs = new URLSearchParams(params as Record<string, string>).toString()
    return request<{ data: unknown[] }>(API_URL, `/modules/${module}/entries?${qs}`)
  },

  createEntry: (module: string, data: unknown) =>
    request(API_URL, `/modules/${module}/entries`, {
      method: 'POST',
      body: JSON.stringify(data),
    }),

  getModuleSummary: (module: string) =>
    request(API_URL, `/modules/${module}/summary`),

  getPriority: () =>
    request<{ data: unknown[] }>(API_URL, '/priority'),

  search: (q: string) =>
    request(API_URL, `/search?q=${encodeURIComponent(q)}`),

  getUserProfile: () =>
    request(API_URL, '/user/profile'),
}

// ── AI Engine (port 9000) ────────────────────────────────────
export const aiApi = {
  chat: (message: string, user_id = 'demo-user') =>
    request<{ data: { role: string; content: string } }>(AI_URL, '/chat', {
      method: 'POST',
      body: JSON.stringify({ message, user_id }),
    }),

  computePriority: (user_id = 'demo-user') =>
    request<{ data: unknown[] }>(AI_URL, '/priority/compute', {
      method: 'POST',
      body: JSON.stringify({ user_id }),
    }),

  generateReflection: (period: string, user_id = 'demo-user') =>
    request(AI_URL, `/reflection/generate?period=${period}`, {
      method: 'POST',
      body: JSON.stringify({ user_id }),
    }),
}
