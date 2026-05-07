// shared/constants/index.ts
// ─────────────────────────────────────────────────────────────
// Module names, thresholds, and other shared constants.
// ─────────────────────────────────────────────────────────────

import type { ModuleName } from '../types/modules'

// ── All 12 module names as an ordered array ──────────────────
export const ALL_MODULES: ModuleName[] = [
  'financial',
  'academic',
  'fitness',
  'sleep',
  'books',
  'good_deeds',
  'bad_deeds',
  'knowledge',
  'games',
  'concepts',
  'exams',
  'friends',
]

// ── Human-readable labels for UI display ────────────────────
export const MODULE_LABELS: Record<ModuleName, string> = {
  financial:  'Financial',
  academic:   'Academic',
  fitness:    'Fitness',
  sleep:      'Sleep',
  books:      'Books',
  good_deeds: 'Good Deeds',
  bad_deeds:  'Bad Deeds',
  knowledge:  'Knowledge',
  games:      'Games',
  concepts:   'Concepts',
  exams:      'Exams',
  friends:    'Friends',
}

// ── Emoji icons for each module (used in UI tiles) ──────────
export const MODULE_ICONS: Record<ModuleName, string> = {
  financial:  '💰',
  academic:   '🎓',
  fitness:    '💪',
  sleep:      '😴',
  books:      '📚',
  good_deeds: '✨',
  bad_deeds:  '⚠️',
  knowledge:  '🧠',
  games:      '🎮',
  concepts:   '💡',
  exams:      '📝',
  friends:    '🤝',
}

// ── Priority Engine thresholds ───────────────────────────────
export const PRIORITY_THRESHOLDS = {
  sleep: {
    low_hours_warning: 6,       // flag if avg sleep < 6h
    low_hours_critical: 5,      // urgent if < 5h
    consecutive_bad_days: 3,    // escalate after 3 days
  },
  financial: {
    savings_gap_percent: 12,    // flag if savings < target by 12%
    high_spend_multiplier: 1.5, // flag if monthly spend > 1.5x avg
  },
  fitness: {
    no_workout_days: 4,         // flag after 4 days no workout
    calorie_deficit_kcal: 500,  // flag if eating 500 kcal below target
  },
  academic: {
    assignment_overdue_days: 2, // flag if overdue > 2 days
    grade_below_percent: 60,    // flag if grade < 60%
  },
} as const

// ── API pagination defaults ──────────────────────────────────
export const DEFAULT_PAGE_LIMIT = 20
export const MAX_PAGE_LIMIT = 100

// ── Reflection schedule ──────────────────────────────────────
export const REFLECTION_SCHEDULE = {
  daily:   '23:30',            // cron: every day at 11:30 PM
  weekly:  'Sunday 23:30',
  monthly: '1st 08:00',
  annual:  'Jan 1st 09:00',
} as const
