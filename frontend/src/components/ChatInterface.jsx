import { useState, useEffect, useRef } from 'react'
import { Send, Image as ImageIcon, MapPin, Loader2, CheckCircle2 } from 'lucide-react'
import MessageBubble from './MessageBubble'
import ImageUpload from './ImageUpload'
import LocationPicker from './LocationPicker'
import DamageTypeSelector from './DamageTypeSelector'
import SeveritySelector from './SeveritySelector'
import { submitReport, sendMessage } from '../utils/api'

function ChatInterface() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [reportData, setReportData] = useState({
    image: null,
    location: null,
    damageType: null,
    severity: null,
    remarks: null
  })
  const [currentStep, setCurrentStep] = useState('greeting')
  const [submitted, setSubmitted] = useState(false)
  const [reportId, setReportId] = useState(null)
  const [showEmailStep, setShowEmailStep] = useState(false)
  const [userEmail, setUserEmail] = useState('')
  const [emailSubmitted, setEmailSubmitted] = useState(false)
  const [reportImageUrl, setReportImageUrl] = useState('')
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const addMessage = (role, content, metadata = {}) => {
    setMessages(prev => [...prev, { role, content, timestamp: new Date(), ...metadata }])
  }

  useEffect(() => {
    // Initialize with greeting message
    addMessage('assistant', 'Hello! I\'m your AI assistant for reporting road damage. I\'ll guide you through the process step by step. Let\'s start by uploading a photo of the road damage.')
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const handleImageUpload = async (file) => {
    setIsLoading(true)
    setReportData(prev => ({ ...prev, image: file }))
    
    addMessage('user', 'Image uploaded', { image: URL.createObjectURL(file) })
    addMessage('assistant', 'Great! I\'m analyzing the image...', { isLoading: true })
    
    try {
      const formData = new FormData()
      formData.append('image', file, file.name)
      
      const response = await sendMessage('/api/analyze-image', formData, true)
      
      if (response.success) {
        addMessage('assistant', response.message || 'Image analyzed successfully. Now, please provide the location of this damage.')
        setCurrentStep('location')
      } else {
        addMessage('assistant', 'I had trouble analyzing the image. Please try uploading again or continue with location.')
        setCurrentStep('location')
      }
    } catch (error) {
      addMessage('assistant', 'There was an error analyzing the image. Let\'s continue with the location.')
      setCurrentStep('location')
    } finally {
      setIsLoading(false)
    }
  }

  const handleLocationSelect = (location) => {
    setReportData(prev => ({ ...prev, location }))
    addMessage('user', `Location: ${location.address || `${location.lat}, ${location.lng}`}`)
    addMessage('assistant', 'Perfect! Now, what type of damage is this?')
    setCurrentStep('damageType')
  }

  const handleDamageTypeSelect = (type) => {
    setReportData(prev => ({ ...prev, damageType: type }))
    addMessage('user', `Damage type: ${type}`)
    addMessage('assistant', 'Good! How severe is this damage?')
    setCurrentStep('severity')
  }

  const handleSeveritySelect = (severity) => {
    setReportData(prev => ({ ...prev, severity }))
    addMessage('user', `Severity: ${severity}`)
    addMessage('assistant', 'Almost done! Would you like to add any additional remarks or details?')
    setCurrentStep('remarks')
  }

  const handleRemarksSubmit = async (remarks) => {
    setReportData(prev => ({ ...prev, remarks: remarks || 'No additional remarks' }))
    
    if (remarks) {
      addMessage('user', `Remarks: ${remarks}`)
    }
    
    addMessage('assistant', 'Thank you! I\'m validating your report and submitting it to the authorities...', { isLoading: true })
    setIsLoading(true)

    try {
      const finalReport = {
        ...reportData,
        remarks: remarks || 'No additional remarks'
      }

      const response = await submitReport(finalReport)
      
      // Backend returns report_id on success
      if (response.report_id) {
        setReportId(response.report_id)
        setReportImageUrl(response.image_url || '') // Capture image URL from response
        setSubmitted(true)
        setShowEmailStep(true)
        const webhookStatus = response.authority_notified
          ? 'The responsible authority has been notified.'
          : 'Note: Webhook notification was not sent (check backend configuration).'
        addMessage('assistant', `✅ Report submitted successfully! Your reference ID is: ${response.report_id}. ${webhookStatus}`, { isLoading: false })
      } else {
        addMessage('assistant', `There was an issue submitting your report: ${response.message || 'Unknown error'}. Please try again.`, { isLoading: false })
      }
    } catch (error) {
      console.error('Submit error:', error)
      const errorMessage = error.response?.data?.detail || error.message || 'Unknown error occurred'
      addMessage('assistant', `An error occurred while submitting your report: ${errorMessage}. Please try again.`, { isLoading: false })
    } finally {
      setIsLoading(false)
    }
  }

  const handleSendMessage = async () => {
    if (!input.trim() || isLoading) return

    const userMessage = input.trim()
    setInput('')
    addMessage('user', userMessage)

    if (currentStep === 'remarks') {
      await handleRemarksSubmit(userMessage)
      return
    }

    setIsLoading(true)
    try {
      const response = await sendMessage('/chat', { message: userMessage, step: currentStep, reportData })
      
      if (response.next_step) {
        setCurrentStep(response.next_step)
      }
      
      if (response.message) {
        addMessage('assistant', response.message)
      }
    } catch (error) {
      addMessage('assistant', 'I apologize, but I encountered an error. Please try again.')
    } finally {
      setIsLoading(false)
    }
  }

  const handleEmailSubmit = async () => {
    if (!userEmail.trim()) return

    setIsLoading(true)
    try {
      const webhookPayload = {
        // Flatten all data to top-level variables for relay.app compatibility
        report_id: reportId,
        location: reportData.location?.address || `${reportData.location?.lat || 0}, ${reportData.location?.lng || 0}`,
        location_lat: reportData.location?.lat || 0,
        location_lng: reportData.location?.lng || 0,
        location_address: reportData.location?.address || '',
        damage_type: reportData.damageType || '',
        severity: reportData.severity || '',
        remarks: reportData.remarks || '',
        image_url: reportImageUrl,

        // CC specific fields
        user_email: userEmail.trim(),
        cc: userEmail.trim(), // Send copy to the user's email

        // Identifier for relay.app conditional logic
        event_type: 'cc_notification'
      }

      const response = await fetch('https://hook.relay.app/api/v1/playbook/cmjzjlqwd00f60pkq0v7peeha/trigger/Cxg6-JhnsGxOXIyySUyXYw', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(webhookPayload)
      })

      if (response.ok) {
        setEmailSubmitted(true)
      }
    } catch (error) {
      console.error('Email submission error:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const renderStepComponent = () => {
    switch (currentStep) {
      case 'greeting':
      case 'image':
        return <ImageUpload onUpload={handleImageUpload} disabled={isLoading} />
      case 'location':
        return <LocationPicker onSelect={handleLocationSelect} disabled={isLoading} />
      case 'damageType':
        return <DamageTypeSelector onSelect={handleDamageTypeSelect} disabled={isLoading} />
      case 'severity':
        return <SeveritySelector onSelect={handleSeveritySelect} disabled={isLoading} />
      case 'remarks':
        return (
          <div className="mt-4">
            <textarea
              className="input-field"
              placeholder="Add any additional details or remarks..."
              rows="3"
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault()
                  handleRemarksSubmit(e.target.value)
                }
              }}
            />
            <button
              onClick={() => handleRemarksSubmit(document.querySelector('textarea').value)}
              className="btn-primary mt-2"
              disabled={isLoading}
            >
              Submit Report
            </button>
          </div>
        )
      default:
        return null
    }
  }

  if (submitted && showEmailStep && !emailSubmitted) {
    return (
      <div className="max-w-2xl mx-auto bg-white rounded-xl shadow-lg p-8 text-center">
        <CheckCircle2 className="w-16 h-16 text-green-500 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-civic-900 mb-2">Report Submitted Successfully!</h2>
        <p className="text-civic-600 mb-4">Your road damage report has been submitted and the responsible authority has been notified.</p>
        <div className="bg-civic-100 rounded-lg p-4 mb-6">
          <p className="text-sm text-civic-600">Reference ID</p>
          <p className="text-xl font-mono font-bold text-primary-600">{reportId}</p>
        </div>

        <div className="border-t border-civic-200 pt-6">
          <h3 className="text-lg font-semibold text-civic-900 mb-2">Stay Updated</h3>
          <p className="text-sm text-civic-600 mb-4">Enter your email to receive a copy of the report notification:</p>
          <div className="flex space-x-2">
            <input
              type="email"
              value={userEmail}
              onChange={(e) => setUserEmail(e.target.value)}
              placeholder="your.email@example.com"
              className="input-field flex-1"
              disabled={isLoading}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && userEmail.trim()) {
                  handleEmailSubmit()
                }
              }}
            />
            <button
              onClick={handleEmailSubmit}
              disabled={isLoading || !userEmail.trim()}
              className="btn-primary"
            >
              {isLoading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Send className="w-5 h-5" />}
            </button>
          </div>
        </div>
      </div>
    )
  }

  if (submitted && emailSubmitted) {
    return (
      <div className="max-w-2xl mx-auto bg-white rounded-xl shadow-lg p-8 text-center">
        <CheckCircle2 className="w-16 h-16 text-green-500 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-civic-900 mb-2">All Set!</h2>
        <p className="text-civic-600 mb-4">Your report has been submitted and a copy has been sent to {userEmail}.</p>
        <div className="bg-civic-100 rounded-lg p-4 mb-4">
          <p className="text-sm text-civic-600">Reference ID</p>
          <p className="text-xl font-mono font-bold text-primary-600">{reportId}</p>
        </div>
        <button
          onClick={() => {
            setMessages([])
            setReportData({ image: null, location: null, damageType: null, severity: null, remarks: null })
            setCurrentStep('greeting')
            setSubmitted(false)
            setReportId(null)
            setShowEmailStep(false)
            setUserEmail('')
            setEmailSubmitted(false)
            addMessage('assistant', 'Hello! I\'m your AI assistant for reporting road damage. I\'ll guide you through the process step by step. Let\'s start by uploading a photo of the road damage.')
          }}
          className="btn-primary"
        >
          Submit Another Report
        </button>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-xl shadow-lg overflow-hidden">
        <div className="bg-gradient-to-r from-primary-600 to-primary-700 p-4 text-white">
          <h2 className="text-xl font-bold">AI Reporting Assistant</h2>
          <p className="text-sm text-primary-100">Guided step-by-step road damage reporting</p>
        </div>
        
        <div className="h-96 overflow-y-auto p-6 bg-civic-50">
          {messages.map((msg, idx) => (
            <MessageBubble key={idx} message={msg} />
          ))}
          {isLoading && (
            <div className="flex items-center space-x-2 text-civic-600">
              <Loader2 className="w-5 h-5 animate-spin" />
              <span>AI is thinking...</span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 bg-white border-t border-civic-200">
          {renderStepComponent()}
          
          {currentStep === 'remarks' && (
            <div className="mt-4 flex space-x-2">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') {
                    handleSendMessage()
                  }
                }}
                placeholder="Type your remarks or press Enter to submit..."
                className="input-field flex-1"
                disabled={isLoading}
              />
              <button
                onClick={handleSendMessage}
                disabled={isLoading || !input.trim()}
                className="btn-primary"
              >
                <Send className="w-5 h-5" />
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default ChatInterface

