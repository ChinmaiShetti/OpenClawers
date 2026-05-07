'use client'
// Reflection page — shows AI-generated daily/weekly/monthly reflections

import { useState } from 'react'
import { Sparkles, Loader2 } from 'lucide-react'
import { aiApi } from '@/lib/api'
import Link from 'next/link'

type Period = 'daily' | 'weekly' | 'monthly' | 'annual'

interface ReflectionResult {
  period: Period
  narrative: string
  highlights: string[]
  concerns: string[]
  generated_at: string
}

export default function ReflectionPage() {
  const [period, setPeriod] = useState<Period>('daily')
  const [result, setResult] = useState<ReflectionResult | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function generate() {
    setLoading(true)
    setError('')
    try {
      const res: { data: ReflectionResult } = await aiApi.generateReflection(period) as { data: ReflectionResult }
      setResult(res.data)
    } catch {
      setError('Could not generate reflection. Make sure the AI engine is running on port 9000.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-100 max-w-3xl mx-auto px-4 py-8">
      <Link href="/dashboard" className="text-xs text-slate-500 hover:text-slate-300 mb-4 block">← Dashboard</Link>
      <h1 className="text-2xl font-bold mb-6 flex items-center gap-2"><Sparkles className="text-violet-400"/> Reflections</h1>

      <div className="flex gap-2 mb-6">
        {(['daily', 'weekly', 'monthly', 'annual'] as Period[]).map(p => (
          <button key={p} onClick={() => setPeriod(p)}
            className={`px-4 py-1.5 rounded-full text-xs font-medium transition-all ${
              period === p ? 'bg-violet-500 text-white' : 'glass text-slate-400 hover:text-slate-200'
            }`}>{p.charAt(0).toUpperCase() + p.slice(1)}
          </button>
        ))}
        <button onClick={generate} disabled={loading}
          className="ml-auto flex items-center gap-2 bg-violet-500 hover:bg-violet-400 disabled:opacity-40 text-white px-4 py-1.5 rounded-full text-xs font-medium transition-all">
          {loading ? <Loader2 size={12} className="animate-spin"/> : <Sparkles size={12}/>}
          Generate
        </button>
      </div>

      {error && <p className="text-red-400 text-sm mb-4">{error}</p>}

      {result ? (
        <div className="space-y-4 animate-slide-up">
          <div className="glass rounded-xl p-5">
            <h2 className="text-sm font-semibold text-violet-400 mb-3">Narrative</h2>
            <p className="text-sm text-slate-300 leading-relaxed">{result.narrative}</p>
          </div>
          <div className="grid grid-cols-2 gap-3">
            <div className="glass rounded-xl p-4">
              <h3 className="text-xs font-semibold text-emerald-400 mb-2">✨ Highlights</h3>
              <ul className="space-y-1">{result.highlights.map((h, i) => <li key={i} className="text-xs text-slate-400">{h}</li>)}</ul>
            </div>
            <div className="glass rounded-xl p-4">
              <h3 className="text-xs font-semibold text-amber-400 mb-2">⚠️ Concerns</h3>
              <ul className="space-y-1">{result.concerns.map((c, i) => <li key={i} className="text-xs text-slate-400">{c}</li>)}</ul>
            </div>
          </div>
        </div>
      ) : (
        !loading && (
          <div className="glass rounded-xl p-12 text-center text-slate-500">
            <Sparkles size={32} className="mx-auto mb-3 text-violet-500"/>
            <p>Select a period and click <strong>Generate</strong> to get your AI reflection.</p>
          </div>
        )
      )}
    </div>
  )
}
