// hooks/useModuleData.ts — Generic hook for any module
'use client'
import { useState, useEffect, useCallback } from 'react'
import { api } from '@/lib/api'

export function useModuleData(module: string, user_id = 'demo-user') {
  const [entries, setEntries] = useState<unknown[]>([])
  const [summary, setSummary] = useState<unknown>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const load = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const [entriesRes, summaryRes] = await Promise.all([
        api.getEntries(module, { user_id }),
        api.getModuleSummary(module),
      ])
      setEntries(entriesRes.data)
      setSummary(summaryRes)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Failed to load data')
    } finally {
      setLoading(false)
    }
  }, [module, user_id])

  useEffect(() => { load() }, [load])

  const create = async (data: unknown) => {
    await api.createEntry(module, { ...data as object, user_id })
    await load()
  }

  return { entries, summary, loading, error, refetch: load, create }
}
