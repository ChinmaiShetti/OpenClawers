// shared/types/api.ts
// ─────────────────────────────────────────────────────────────
// HTTP request/response shapes for every endpoint.
// Agreed upon by all 3 team members on Day 0.
// ─────────────────────────────────────────────────────────────

import type { ModuleName, ModuleEntry, PriorityItem, ReflectionPeriod, ReflectionResult } from './modules'

// ── Generic wrapper ──────────────────────────────────────────
export interface ApiResponse<T> {
  data: T
  error?: string
  meta?: {
    total?: number
    limit?: number
    offset?: number
  }
}

// ── Chat ─────────────────────────────────────────────────────
export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
  timestamp?: string
}

export interface ChatRequest {
  messages: ChatMessage[]
  user_id: string
  stream?: boolean
}

export interface ChatResponse {
  message: ChatMessage
  context_used?: string[]         // list of module names the AI drew context from
}

// ── Module CRUD ──────────────────────────────────────────────
export interface CreateEntryRequest {
  module: ModuleName
  data: Record<string, unknown>
  user_id: string
}

export type CreateEntryResponse = ApiResponse<ModuleEntry>
export type ListEntriesResponse = ApiResponse<ModuleEntry[]>

// ── Module Summary (aggregated stats for dashboard) ─────────
export interface ModuleSummary {
  module: ModuleName
  entry_count: number
  last_entry_at?: string
  summary_data: Record<string, unknown>   // module-specific aggregations
}

export type ModuleSummaryResponse = ApiResponse<ModuleSummary>

// ── Priority ─────────────────────────────────────────────────
export type PriorityResponse = ApiResponse<PriorityItem[]>

// ── Reflection ───────────────────────────────────────────────
export interface ReflectionRequest {
  period: ReflectionPeriod
  user_id: string
}

export type ReflectionResponse = ApiResponse<ReflectionResult>

// ── Search ───────────────────────────────────────────────────
export interface SearchResult {
  entry: ModuleEntry
  score: number                   // semantic similarity 0-1
  excerpt: string
}

export type SearchResponse = ApiResponse<SearchResult[]>

// ── User Profile ─────────────────────────────────────────────
export interface UserProfile {
  user_id: string
  name: string
  email?: string
  phone?: string                  // for WhatsApp nudges
  preferences: {
    nudge_enabled: boolean
    nudge_time: string            // e.g. "08:00"
    timezone: string
  }
}

export type UserProfileResponse = ApiResponse<UserProfile>

// ── Meeting ──────────────────────────────────────────────────
export interface MeetingPrepRequest {
  calendar_event_id: string
  user_id: string
}

export interface MeetingPrepResponse {
  template: string
  attendees: string[]
  agenda_items: string[]
}

export interface MeetingProcessRequest {
  notes: string
  user_id: string
}

export interface MeetingProcessResponse {
  action_items: Array<{ task: string; owner?: string; due?: string }>
  summary: string
}
