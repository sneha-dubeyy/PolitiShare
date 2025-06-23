import React, { useState, useEffect } from 'react'
import './index.css'

function App() {
  const [apiStatus, setApiStatus] = useState('Testing...')
  const [backendData, setBackendData] = useState(null)

  // Test backend connection
  useEffect(() => {
    const testAPI = async () => {
      try {
        const response = await fetch('https://politishare-production.up.railway.app/health')
        if (response.ok) {
          const data = await response.json()
          setApiStatus('Connected ✅')
          setBackendData(data)
        } else {
          setApiStatus('Connection Failed ❌')
        }
      } catch (error) {
        setApiStatus('Connection Failed ❌')
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
          
          <button className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105">
            🚀 Take Political Survey (Coming Soon)
          </button>
        </div>
        
        <div className="border-t border-gray-200 pt-4">
          <div className="text-sm text-gray-500 space-y-2">
            <div className="flex items-center justify-center space-x-2">
              <span className="w-2 h-2 bg-green-500 rounded-full"></span>
              <span>Frontend: Deployed ✅</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <span className={`w-2 h-2 rounded-full ${apiStatus.includes('✅') ? 'bg-green-500' : 'bg-red-500'}`}></span>
              <span>Backend: {apiStatus}</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <span className="w-2 h-2 bg-green-500 rounded-full"></span>
              <span>Database: Supabase ✅</span>
            </div>
            {backendData && (
              <div className="mt-4 p-3 bg-gray-50 rounded-lg text-xs">
                <div>Environment: {backendData.environment}</div>
                <div>Project: {backendData.project}</div>
                <div>Status: {backendData.status}</div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
