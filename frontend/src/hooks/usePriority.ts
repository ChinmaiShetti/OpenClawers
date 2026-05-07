// hooks/usePriority.ts — Fetch priority list from AI engine
'use client'
import { useState, useEffect } from 'react'
import { aiApi } from '@/lib/api'

export function usePriority(user_id = 'demo-user') {
  const [priority, setPriority] = useState<unknown[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    aiApi.computePriority(user_id)
      .then(res => setPriority(res.data))
      .catch(e => setError(e.message))
      .finally(() => setLoading(false))
  }, [user_id])

  return { priority, loading, error }
}
