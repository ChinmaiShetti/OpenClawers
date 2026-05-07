'use client'
// Dashboard — main view for OpenClaw
// Shows: greeting, priority list, 12 module tiles, daily snapshot

import { useState } from 'react'
import Link from 'next/link'
import {
  Wallet, GraduationCap, Dumbbell, Moon, BookOpen,
  Heart, AlertTriangle, Brain, Gamepad2, Lightbulb,
  ClipboardList, Users, MessageSquare, BarChart2,
  ChevronRight, Zap, TrendingUp, TrendingDown, Minus,
} from 'lucide-react'

// ── Types ─────────────────────────────────────────────────────
type Urgency = 'high' | 'medium' | 'low'

interface PriorityItem {
  module: string
  title: string
  description: string
  urgency: Urgency
  score: number
}

interface ModuleTile {
  name: string
  label: string
  icon: React.ReactNode
  href: string
  metric: string
  trend: 'up' | 'down' | 'flat'
  color: string
}

// ── Mock data (replace with API calls via useModuleData) ──────
const PRIORITY_MOCK: PriorityItem[] = [
  { module: 'sleep',     title: 'Sleep Deficit Alert',   description: 'Avg 5.2h over last 3 days — below 6h threshold', urgency: 'high',   score: 92 },
  { module: 'financial', title: 'Savings Gap',           description: 'Savings 12% below monthly target of ₹15,000',   urgency: 'high',   score: 85 },
  { module: 'academic',  title: 'Assignment Overdue',    description: 'DSA assignment due 2 days ago',                  urgency: 'high',   score: 80 },
  { module: 'fitness',   title: 'No Workout in 4 Days',  description: 'Last workout was Monday — streak at risk',       urgency: 'medium', score: 60 },
  { module: 'books',     title: 'Reading Streak',        description: 'Keep up the 12-day reading streak tonight',      urgency: 'low',    score: 30 },
]

const MODULE_TILES: ModuleTile[] = [
  { name: 'financial',  label: 'Financial',   icon: <Wallet size={20}/>,        href: '/modules/financial',  metric: '₹42,300 saved', trend: 'up',   color: '#10b981' },
  { name: 'academic',   label: 'Academic',    icon: <GraduationCap size={20}/>, href: '/modules/academic',   metric: '3.8 GPA',        trend: 'up',   color: '#6366f1' },
  { name: 'fitness',    label: 'Fitness',     icon: <Dumbbell size={20}/>,      href: '/modules/fitness',    metric: '4 workouts/wk',  trend: 'down', color: '#f59e0b' },
  { name: 'sleep',      label: 'Sleep',       icon: <Moon size={20}/>,          href: '/modules/sleep',      metric: '5.2h avg',       trend: 'down', color: '#8b5cf6' },
  { name: 'books',      label: 'Books',       icon: <BookOpen size={20}/>,      href: '/modules/books',      metric: '12 books YTD',   trend: 'up',   color: '#0ea5e9' },
  { name: 'good_deeds', label: 'Good Deeds',  icon: <Heart size={20}/>,         href: '/modules/good-deeds', metric: '24 this month',  trend: 'up',   color: '#ec4899' },
  { name: 'bad_deeds',  label: 'Bad Deeds',   icon: <AlertTriangle size={20}/>, href: '/modules/bad-deeds',  metric: '3 this week',    trend: 'down', color: '#ef4444' },
  { name: 'knowledge',  label: 'Knowledge',   icon: <Brain size={20}/>,         href: '/modules/knowledge',  metric: '47 entries',     trend: 'up',   color: '#14b8a6' },
  { name: 'games',      label: 'Games',       icon: <Gamepad2 size={20}/>,      href: '/modules/games',      metric: '8h this week',   trend: 'flat', color: '#a855f7' },
  { name: 'concepts',   label: 'Concepts',    icon: <Lightbulb size={20}/>,     href: '/modules/concepts',   metric: '31 concepts',    trend: 'up',   color: '#f97316' },
  { name: 'exams',      label: 'Exams',       icon: <ClipboardList size={20}/>, href: '/modules/exams',      metric: '2 upcoming',     trend: 'flat', color: '#06b6d4' },
  { name: 'friends',    label: 'Friends',     icon: <Users size={20}/>,         href: '/modules/friends',    metric: '5 meetups/mo',   trend: 'up',   color: '#84cc16' },
]

const URGENCY_STYLES: Record<Urgency, string> = {
  high:   'bg-red-500/10 text-red-400 border border-red-500/30',
  medium: 'bg-amber-500/10 text-amber-400 border border-amber-500/30',
  low:    'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30',
}

function TrendIcon({ trend }: { trend: 'up' | 'down' | 'flat' }) {
  if (trend === 'up')   return <TrendingUp  size={14} className="text-emerald-400"/>
  if (trend === 'down') return <TrendingDown size={14} className="text-red-400"/>
  return <Minus size={14} className="text-slate-400"/>
}

export default function DashboardPage() {
  const [activeTab, setActiveTab] = useState<'priority' | 'modules'>('priority')

  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-100">

      {/* ── Top nav ────────────────────────────────────────── */}
      <nav className="sticky top-0 z-50 glass border-b border-slate-700/50 px-6 py-3 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-sky-500 to-violet-600 flex items-center justify-center text-white font-bold text-sm">
            OC
          </div>
          <span className="font-semibold text-slate-100 tracking-tight">OpenClaw</span>
        </div>
        <div className="flex items-center gap-4 text-sm text-slate-400">
          <Link href="/dashboard"  className="text-sky-400 font-medium">Dashboard</Link>
          <Link href="/chat"       className="hover:text-slate-200 transition-colors flex items-center gap-1"><MessageSquare size={14}/>Chat</Link>
          <Link href="/reflection" className="hover:text-slate-200 transition-colors flex items-center gap-1"><BarChart2 size={14}/>Reflect</Link>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-gradient-to-br from-violet-500 to-sky-500 flex items-center justify-center text-xs font-bold">A</div>
          <span className="text-sm text-slate-300 hidden sm:block">Arjun</span>
        </div>
      </nav>

      <main className="max-w-6xl mx-auto px-4 sm:px-6 py-8 space-y-8 animate-fade-in">

        {/* ── Greeting ───────────────────────────────────────── */}
        <div>
          <h1 className="text-3xl font-bold text-gradient mb-1">Good evening, Arjun 👋</h1>
          <p className="text-slate-400 text-sm">Thursday · 7 May 2026 · Your focus score today: <span className="text-sky-400 font-semibold">72/100</span></p>
        </div>

        {/* ── Daily Snapshot ─────────────────────────────────── */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {[
            { label: 'Sleep',    value: '5.2h', icon: <Moon size={16}/>,    color: '#8b5cf6', warn: true },
            { label: 'Workout',  value: '4 days ago', icon: <Dumbbell size={16}/>, color: '#f59e0b', warn: true },
            { label: 'Books',    value: '22 pages',   icon: <BookOpen size={16}/>, color: '#0ea5e9', warn: false },
            { label: 'Savings',  value: '₹42,300',    icon: <Wallet size={16}/>,   color: '#10b981', warn: false },
          ].map(s => (
            <div key={s.label} className="glass rounded-xl p-4 flex flex-col gap-2">
              <div className="flex items-center justify-between">
                <span style={{ color: s.color }}>{s.icon}</span>
                {s.warn && <span className="text-xs text-red-400 font-medium">!</span>}
              </div>
              <p className="text-xl font-bold text-slate-100">{s.value}</p>
              <p className="text-xs text-slate-500">{s.label}</p>
            </div>
          ))}
        </div>

        {/* ── Tabs ───────────────────────────────────────────── */}
        <div className="flex gap-1 p-1 bg-slate-800/50 rounded-xl w-fit">
          {(['priority', 'modules'] as const).map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`px-5 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === tab
                  ? 'bg-sky-500 text-white shadow-lg shadow-sky-500/25'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              {tab === 'priority' ? '⚡ Priority List' : '📊 All Modules'}
            </button>
          ))}
        </div>

        {/* ── Priority List ──────────────────────────────────── */}
        {activeTab === 'priority' && (
          <div className="space-y-3 animate-slide-up">
            {PRIORITY_MOCK.map((item, i) => (
              <div key={i} className="glass rounded-xl p-4 flex items-center gap-4 hover:border-sky-500/40 transition-all cursor-pointer group">
                <div className="text-2xl font-bold text-slate-600 w-7 shrink-0">#{i + 1}</div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-0.5">
                    <span className="font-semibold text-slate-100 text-sm">{item.title}</span>
                    <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${URGENCY_STYLES[item.urgency]}`}>
                      {item.urgency}
                    </span>
                  </div>
                  <p className="text-xs text-slate-400 truncate">{item.description}</p>
                </div>
                <div className="flex items-center gap-3 shrink-0">
                  <div className="text-right">
                    <div className="text-lg font-bold text-slate-200">{item.score}</div>
                    <div className="text-xs text-slate-500">score</div>
                  </div>
                  <ChevronRight size={16} className="text-slate-600 group-hover:text-sky-400 transition-colors"/>
                </div>
              </div>
            ))}
            <div className="text-center pt-2">
              <Link href="/chat" className="text-xs text-sky-400 hover:text-sky-300 transition-colors">
                Ask OpenClaw AI to explain these priorities →
              </Link>
            </div>
          </div>
        )}

        {/* ── Module Tiles ───────────────────────────────────── */}
        {activeTab === 'modules' && (
          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3 animate-slide-up">
            {MODULE_TILES.map(tile => (
              <Link key={tile.name} href={tile.href}>
                <div className="glass rounded-xl p-4 hover:scale-[1.02] hover:shadow-lg transition-all duration-200 cursor-pointer group h-full">
                  <div className="flex items-center justify-between mb-3">
                    <div className="w-8 h-8 rounded-lg flex items-center justify-center" style={{ backgroundColor: `${tile.color}20`, color: tile.color }}>
                      {tile.icon}
                    </div>
                    <TrendIcon trend={tile.trend}/>
                  </div>
                  <p className="text-sm font-semibold text-slate-200 mb-0.5">{tile.label}</p>
                  <p className="text-xs text-slate-500">{tile.metric}</p>
                </div>
              </Link>
            ))}
          </div>
        )}

      </main>
    </div>
  )
}
