import React from 'react'
import './index.css'

function App() {
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
          <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105">
            Take Political Survey
          </button>
          
          <button className="w-full border-2 border-blue-600 text-blue-600 hover:bg-blue-600 hover:text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200">
            View Community Results
          </button>
          
          <button className="w-full bg-purple-600 hover:bg-purple-700 text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105">
            Join Social Feed
          </button>
        </div>
        
        <div className="border-t border-gray-200 pt-4">
          <div className="text-sm text-gray-500 space-y-1">
            <div className="flex items-center justify-center space-x-2">
              <span className="w-2 h-2 bg-green-500 rounded-full"></span>
              <span>Frontend deployed successfully!</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <span className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></span>
              <span>Backend integration ready...</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
