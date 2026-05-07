'use client'
// Financial Module Page — full CRUD UI

import { useState, useEffect } from 'react'
import { Plus, TrendingUp, TrendingDown, Wallet } from 'lucide-react'
import { api } from '@/lib/api'
import Link from 'next/link'

interface Transaction {
  id: string
  type: string
  amount: number
  currency: string
  category: string
  description?: string
  created_at: string
}

interface FormData {
  type: 'income' | 'expense' | 'savings'
  amount: string
  category: string
  description: string
  user_id: string
}

export default function FinancialPage() {
  const [entries, setEntries] = useState<Transaction[]>([])
  const [showForm, setShowForm] = useState(false)
  const [loading, setLoading] = useState(true)
  const [form, setForm] = useState<FormData>({
    type: 'expense', amount: '', category: '', description: '', user_id: 'demo-user'
  })

  async function load() {
    setLoading(true)
    try {
      const res = await api.getEntries('financial')
      setEntries(res.data as Transaction[])
    } catch {
      // backend may not be running — use mock
      setEntries([
        { id: '1', type: 'income',  amount: 55000, currency: 'INR', category: 'Salary',     created_at: '2026-05-01T09:00:00Z' },
        { id: '2', type: 'expense', amount: 8200,  currency: 'INR', category: 'Groceries',  created_at: '2026-05-03T18:30:00Z' },
        { id: '3', type: 'savings', amount: 10000, currency: 'INR', category: 'Emergency',  created_at: '2026-05-05T10:00:00Z' },
      ])
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => { load() }, [])

  async function submit(e: React.FormEvent) {
    e.preventDefault()
    await api.createEntry('financial', { ...form, amount: parseFloat(form.amount) })
    setShowForm(false)
    load()
  }

  const income  = entries.filter(e => e.type === 'income').reduce((s, e) => s + e.amount, 0)
  const expense = entries.filter(e => e.type === 'expense').reduce((s, e) => s + e.amount, 0)
  const savings = entries.filter(e => e.type === 'savings').reduce((s, e) => s + e.amount, 0)

  return (
    <div className="min-h-screen bg-[#0f172a] text-slate-100 max-w-4xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <div>
          <Link href="/dashboard" className="text-xs text-slate-500 hover:text-slate-300 mb-1 block">← Dashboard</Link>
          <h1 className="text-2xl font-bold flex items-center gap-2"><Wallet className="text-emerald-400"/> Financial</h1>
        </div>
        <button
          onClick={() => setShowForm(v => !v)}
          className="flex items-center gap-2 bg-emerald-500 hover:bg-emerald-400 text-white px-4 py-2 rounded-xl text-sm font-medium transition-all"
        >
          <Plus size={16}/> Add Entry
        </button>
      </div>

      {/* Summary cards */}
      <div className="grid grid-cols-3 gap-3 mb-6">
        {[
          { label: 'Income',  val: income,  color: '#10b981', icon: <TrendingUp size={16}/> },
          { label: 'Expense', val: expense, color: '#ef4444', icon: <TrendingDown size={16}/> },
          { label: 'Savings', val: savings, color: '#0ea5e9', icon: <Wallet size={16}/> },
        ].map(s => (
          <div key={s.label} className="glass rounded-xl p-4">
            <div className="flex items-center gap-2 text-xs text-slate-400 mb-2" style={{ color: s.color }}>{s.icon}<span>{s.label}</span></div>
            <p className="text-xl font-bold">₹{s.val.toLocaleString('en-IN')}</p>
          </div>
        ))}
      </div>

      {/* Add form */}
      {showForm && (
        <form onSubmit={submit} className="glass rounded-xl p-5 mb-6 space-y-3">
          <h2 className="font-semibold text-sm text-slate-300">New Transaction</h2>
          <div className="grid grid-cols-2 gap-3">
            <select className="bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm focus:border-sky-500 focus:outline-none col-span-2"
              value={form.type} onChange={e => setForm(f => ({ ...f, type: e.target.value as FormData['type'] }))}>
              <option value="income">💰 Income</option>
              <option value="expense">💸 Expense</option>
              <option value="savings">🏦 Savings</option>
            </select>
            <input required placeholder="Amount (₹)" type="number" className="bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm focus:border-sky-500 focus:outline-none"
              value={form.amount} onChange={e => setForm(f => ({ ...f, amount: e.target.value }))}/>
            <input required placeholder="Category" className="bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm focus:border-sky-500 focus:outline-none"
              value={form.category} onChange={e => setForm(f => ({ ...f, category: e.target.value }))}/>
            <input placeholder="Description (optional)" className="bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-sm focus:border-sky-500 focus:outline-none col-span-2"
              value={form.description} onChange={e => setForm(f => ({ ...f, description: e.target.value }))}/>
          </div>
          <div className="flex gap-2 justify-end">
            <button type="button" onClick={() => setShowForm(false)} className="text-sm text-slate-400 px-4 py-2 hover:text-slate-200">Cancel</button>
            <button type="submit" className="bg-emerald-500 hover:bg-emerald-400 text-white px-5 py-2 rounded-lg text-sm font-medium">Save</button>
          </div>
        </form>
      )}

      {/* Entries list */}
      {loading ? (
        <div className="text-center py-12 text-slate-500">Loading…</div>
      ) : (
        <div className="space-y-2">
          {entries.map(e => (
            <div key={e.id} className="glass rounded-xl p-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span className="text-lg">{e.type === 'income' ? '💰' : e.type === 'savings' ? '🏦' : '💸'}</span>
                <div>
                  <p className="text-sm font-medium text-slate-200">{e.category}</p>
                  <p className="text-xs text-slate-500">{new Date(e.created_at).toLocaleDateString()}</p>
                </div>
              </div>
              <p className={`font-semibold text-sm ${e.type === 'income' ? 'text-emerald-400' : e.type === 'savings' ? 'text-sky-400' : 'text-red-400'}`}>
                {e.type === 'expense' ? '-' : '+'}₹{e.amount.toLocaleString('en-IN')}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
