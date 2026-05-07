'use client'
import Link from 'next/link'

export default function ConceptsPage() {
  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-100 max-w-4xl mx-auto px-4 py-8">
      <Link href="/dashboard" className="text-xs text-slate-500 hover:text-slate-300 mb-4 block">Back to Dashboard</Link>
      <h1 className="text-2xl font-bold mb-2 text-orange-400">Concepts Module</h1>
      <p className="text-slate-400 text-sm mb-8">Log and review your data here.</p>
      <div className="bg-slate-800 border border-slate-700 rounded-xl p-8 text-center text-slate-500">
        <p className="font-medium text-slate-300 mb-2">Concepts — coming soon</p>
        <p className="text-sm">Person 1: Build this module page. See financial/page.tsx as reference.</p>
      </div>
    </div>
  )
}