'use client'
// AI Chat page — conversational interface with OpenClaw AI

import { useState, useRef, useEffect } from 'react'
import { Send, Bot, User, Loader2 } from 'lucide-react'
import { aiApi } from '@/lib/api'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', content: "Hi Arjun! I'm OpenClaw AI. I know everything about your 12 life modules. What would you like to explore today?" }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  async function send() {
    if (!input.trim() || loading) return
    const userMsg = input.trim()
    setInput('')
    setMessages(m => [...m, { role: 'user', content: userMsg }])
    setLoading(true)
    try {
      const res = await aiApi.chat(userMsg)
      setMessages(m => [...m, { role: 'assistant', content: res.data.content }])
    } catch {
      setMessages(m => [...m, { role: 'assistant', content: '⚠️ Could not reach AI engine. Make sure it\'s running on port 9000.' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#0f172a] flex flex-col">
      {/* Header */}
      <div className="glass border-b border-slate-700/50 px-6 py-4 flex items-center gap-3">
        <div className="w-9 h-9 rounded-full bg-gradient-to-br from-sky-500 to-violet-600 flex items-center justify-center">
          <Bot size={18} className="text-white"/>
        </div>
        <div>
          <h1 className="font-semibold text-slate-100">OpenClaw AI</h1>
          <p className="text-xs text-emerald-400">● Online</p>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4 max-w-3xl w-full mx-auto">
        {messages.map((msg, i) => (
          <div key={i} className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
            {msg.role === 'assistant' && (
              <div className="w-8 h-8 rounded-full bg-gradient-to-br from-sky-500 to-violet-600 flex items-center justify-center shrink-0">
                <Bot size={14} className="text-white"/>
              </div>
            )}
            <div className={`max-w-[75%] rounded-2xl px-4 py-3 text-sm leading-relaxed ${
              msg.role === 'user'
                ? 'bg-sky-500 text-white rounded-tr-sm'
                : 'glass text-slate-200 rounded-tl-sm'
            }`}>
              {msg.content}
            </div>
            {msg.role === 'user' && (
              <div className="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center shrink-0">
                <User size={14} className="text-slate-300"/>
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div className="flex gap-3 items-center text-slate-400 text-sm">
            <Loader2 size={16} className="animate-spin"/>
            OpenClaw is thinking…
          </div>
        )}
        <div ref={bottomRef}/>
      </div>

      {/* Input */}
      <div className="glass border-t border-slate-700/50 px-4 py-4">
        <div className="max-w-3xl mx-auto flex gap-3">
          <input
            className="flex-1 bg-slate-800/60 border border-slate-700 rounded-xl px-4 py-3 text-sm text-slate-100 placeholder:text-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
            placeholder="Ask anything about your life data…"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && !e.shiftKey && send()}
          />
          <button
            onClick={send}
            disabled={!input.trim() || loading}
            className="w-12 h-12 rounded-xl bg-sky-500 hover:bg-sky-400 disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center transition-all"
          >
            <Send size={18} className="text-white"/>
          </button>
        </div>
      </div>
    </div>
  )
}
