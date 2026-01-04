import { useState } from 'react'
import ChatInterface from './components/ChatInterface'
import Header from './components/Header'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-civic-50 via-primary-50 to-civic-100">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <ChatInterface />
      </main>
    </div>
  )
}

export default App


