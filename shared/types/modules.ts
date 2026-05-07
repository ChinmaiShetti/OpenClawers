// shared/types/modules.ts
// ─────────────────────────────────────────────────────────────
// THE SOURCE OF TRUTH for all module names and data shapes.
// Agreed upon by all 3 team members on Day 0.
// Do NOT edit without a team discussion.
// ─────────────────────────────────────────────────────────────

export type ModuleName =
  | 'financial'
  | 'good_deeds'
  | 'bad_deeds'
  | 'academic'
  | 'exams'
  | 'fitness'
  | 'knowledge'
  | 'sleep'
  | 'games'
  | 'concepts'
  | 'books'
  | 'friends'

// ── Generic entry shape (all 12 modules share this wrapper) ──
export interface ModuleEntry {
  id: string
  module: ModuleName
  user_id: string
  data: Record<string, unknown>   // module-specific payload (see below)
  created_at: string              // ISO 8601
}

// ── Priority Engine output ───────────────────────────────────
export interface PriorityItem {
  module: ModuleName
  title: string
  description: string
  urgency: 'high' | 'medium' | 'low'
  impact: 'high' | 'medium' | 'low'
  score: number                   // 0–100 composite (urgency × impact × recency)
}

// ── Reflection output ────────────────────────────────────────
export type ReflectionPeriod = 'daily' | 'weekly' | 'monthly' | 'annual'

export interface ReflectionResult {
  period: ReflectionPeriod
  narrative: string               // Long-form AI-generated text
  highlights: string[]            // Top positive moments
  concerns: string[]              // Things that need attention
  generated_at: string            // ISO 8601
}

// ── Module-specific data payloads ───────────────────────────
// These are the `data` field shapes — used for type narrowing.

export interface FinancialData {
  type: 'income' | 'expense' | 'savings'
  amount: number
  currency: string
  category: string
  description?: string
}

export interface SleepData {
  duration_hours: number
  quality: 1 | 2 | 3 | 4 | 5     // 1=terrible, 5=excellent
  bedtime: string                 // ISO time
  wake_time: string               // ISO time
  notes?: string
}

export interface FitnessData {
  type: 'workout' | 'food' | 'body_metric'
  workout_type?: string
  duration_minutes?: number
  calories?: number
  weight_kg?: number
  notes?: string
}

export interface AcademicData {
  type: 'course' | 'assignment' | 'grade'
  course_name: string
  score?: number
  max_score?: number
  description?: string
}

export interface BookData {
  title: string
  author: string
  pages_read: number
  notes?: string
  rating?: 1 | 2 | 3 | 4 | 5
}
