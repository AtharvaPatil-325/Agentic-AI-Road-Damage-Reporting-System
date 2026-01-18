import axios from 'axios'

// In development, use relative URLs to go through Vite proxy
// In production, use the full API URL
const API_URL = import.meta.env.VITE_API_URL || ''

const api = axios.create({
  baseURL: API_URL || (import.meta.env.DEV ? '' : 'http://localhost:8000'),
})

export const sendMessage = async (endpoint, data, isFormData = false) => {
  try {
    const config = {
      headers: isFormData 
        ? {} // Let axios/browser automatically set Content-Type for FormData
        : { 'Content-Type': 'application/json' }
    }
    
    const response = await api.post(endpoint, data, config)
    return response.data
  } catch (error) {
    console.error('API Error:', error)
    if (error.response) {
      console.error('Response data:', error.response.data)
      console.error('Response status:', error.response.status)
    }
    throw error
  }
}

export const submitReport = async (reportData) => {
  try {
    const formData = new FormData()
    
    if (reportData.image) {
      formData.append('image', reportData.image)
    }
    
    formData.append('location', JSON.stringify(reportData.location))
    formData.append('damage_type', reportData.damageType)
    formData.append('severity', reportData.severity)
    formData.append('remarks', reportData.remarks || '')
    
    const response = await api.post('/api/reports/submit', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    
    return response.data
  } catch (error) {
    console.error('Submit Error:', error)
    throw error
  }
}

export default api

