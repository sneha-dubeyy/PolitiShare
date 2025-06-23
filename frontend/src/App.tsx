import React, { useState, useEffect } from 'react'
import './index.css'

function App() {
  const [apiStatus, setApiStatus] = useState('Testing...')
  const [backendData, setBackendData] = useState(null)

  // Test backend connection with retry
  useEffect(() => {
    const testAPI = async () => {
      let attempts = 0
      const maxAttempts = 3
      
      while (attempts < maxAttempts) {
        try {
          const response = await fetch('https://politishare-production.up.railway.app/health', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          })
          
          if (response.ok) {
            const data = await response.json()
            setApiStatus('Connected ✅')
            setBackendData(data)
            return
          }
        } catch (error) {
          attempts++
          if (attempts === maxAttempts) {
            console.log('All connection attempts failed:', error)
            setApiStatus('Connection Failed ❌')
          } else {
            // Wait 1 second before retry
            await new Promise(resolve => setTimeout(resolve, 1000))
          }
        }
      }
    }
    
    testAPI()
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white p-8 rounded-xl shadow-xl max-w-lg w-full text-center border border-gray-200">
        <div className="mb-6">
          <h1 className="text-5xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            PolitiShare
          </h1>
          <p className="text-gray-600 text-lg">
            Political Party Prediction & Social Platform
          </p>
        </div>
        
        <div className="space-y-4 mb-6">
          <button 
            onClick={() => window.open('https://politishare-production.up.railway.app/docs', '_blank')}
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105"
          >
            🔗 View API Documentation
          </button>
          
          <button 
            onClick={() => window.open('https://politishare-production.up.railway.app/health', '_blank')}
            className="w-full border-2 border-green-600 text-green-600 hover:bg-green-600 hover:text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200"
          >
            ⚡ Test Backend Health
          </button>
          
          <button 
            onClick={() => window.open('https://politishare-production.up.railway.app/', '_blank')}
            className="w-full border-2 border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200"
          >
            🚀 Test Root Endpoint
          </button>
          
          <button className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105">
            📊 Take Political Survey (Coming Soon)
          </button>
        </div>
        
        <div className="border-t border-gray-200 pt-4">
          <div className="text-sm text-gray-500 space-y-2">
            <div className="flex items-center justify-center space-x-2">
              <span className="w-2 h-2 bg-green-500 rounded-full"></span>
              <span>Frontend: Deployed ✅</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <span className={`w-2 h-2 rounded-full ${
                apiStatus.includes('✅') ? 'bg-green-500' : 
                apiStatus.includes('Testing') ? 'bg-yellow-500 animate-pulse' : 'bg-red-500'
              }`}></span>
              <span>Backend: {apiStatus}</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <span className="w-2 h-2 bg-green-500 rounded-full"></span>
              <span>Database: Supabase ✅</span>
            </div>
            {backendData && (
              <div className="mt-4 p-3 bg-gray-50 rounded-lg text-xs">
                <div>✅ Environment: {backendData.environment}</div>
                <div>✅ Project: {backendData.project}</div>
                <div>✅ Status: {backendData.status}</div>
                <div>✅ Python: {backendData.python_version}</div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
