// shared/types/user.ts

export interface User {
  user_id: string
  name: string
  email?: string
  phone?: string
  created_at: string
}

export interface Session {
  user_id: string
  token: string
  expires_at: string
}
