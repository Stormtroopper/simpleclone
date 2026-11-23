const BASE_URL=import.meta.env.VITE_API_URL ??'http://localhost:8000'
export const api = async <T>(
  path: string,
  options: RequestInit = {},
  token?: string | null,
): Promise<T> => {
  const res = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
  })
  const data = await res.json().catch(() => null)
  if (!res.ok) {
    throw new Error(typeof data?.detail === 'string' ? data.detail : `Request failed (${res.status})`)
  }
  return data
}