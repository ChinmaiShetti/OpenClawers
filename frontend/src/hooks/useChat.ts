// hooks/useChat.ts — Chat state management
'use client'
import { useState } from 'react'
import { aiApi } from '@/lib/api'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

export function useChat(user_id = 'demo-user') {
  const [messages, setMessages] = useState<Message[]>([])
  const [loading, setLoading] = useState(false)

  const send = async (content: string) => {
    setMessages(m => [...m, { role: 'user', content }])
    setLoading(true)
    try {
      const res = await aiApi.chat(content, user_id)
      setMessages(m => [...m, { role: 'assistant', content: res.data.content }])
    } catch (e) {
      setMessages(m => [...m, { role: 'assistant', content: `Error: ${e instanceof Error ? e.message : 'Unknown error'}` }])
    } finally {
      setLoading(false)
    }
  }

  const clear = () => setMessages([])

  return { messages, loading, send, clear }
}
