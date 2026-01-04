import { useState, useEffect } from 'react'
import { MapPin, Navigation } from 'lucide-react'

function LocationPicker({ onSelect, disabled }) {
  const [location, setLocation] = useState(null)
  const [manualMode, setManualMode] = useState(false)
  const [manualLat, setManualLat] = useState('')
  const [manualLng, setManualLng] = useState('')
  const [address, setAddress] = useState('')

  useEffect(() => {
    if (navigator.geolocation) {
      getCurrentLocation()
    }
  }, [])

  const getCurrentLocation = () => {
    if (disabled) return
    
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const loc = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
          address: `${position.coords.latitude.toFixed(6)}, ${position.coords.longitude.toFixed(6)}`
        }
        setLocation(loc)
        reverseGeocode(loc.lat, loc.lng)
      },
      (error) => {
        console.error('Geolocation error:', error)
        setManualMode(true)
      }
    )
  }

  const reverseGeocode = async (lat, lng) => {
    try {
      // Using OpenStreetMap Nominatim API for reverse geocoding
      const response = await fetch(
        `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`,
        {
          headers: {
            'User-Agent': 'RoadDamageReporter/1.0'
          }
        }
      )
      const data = await response.json()
      if (data.display_name) {
        setAddress(data.display_name)
        setLocation(prev => ({ ...prev, address: data.display_name }))
      }
    } catch (error) {
      console.error('Reverse geocoding error:', error)
    }
  }

  const handleManualSubmit = () => {
    const lat = parseFloat(manualLat)
    const lng = parseFloat(manualLng)
    
    if (isNaN(lat) || isNaN(lng)) {
      alert('Please enter valid coordinates')
      return
    }
    
    const loc = {
      lat,
      lng,
      address: address || `${lat}, ${lng}`
    }
    setLocation(loc)
    if (!address) {
      reverseGeocode(lat, lng)
    }
  }

  const handleConfirm = () => {
    if (location) {
      onSelect(location)
    }
  }

  return (
    <div className="space-y-4">
      {!location ? (
        <>
          {!manualMode ? (
            <div className="space-y-4">
              <button
                onClick={getCurrentLocation}
                disabled={disabled}
                className="btn-primary w-full flex items-center justify-center space-x-2"
              >
                <Navigation className="w-5 h-5" />
                <span>Use Current Location</span>
              </button>
              <button
                onClick={() => setManualMode(true)}
                disabled={disabled}
                className="btn-secondary w-full"
              >
                Enter Location Manually
              </button>
            </div>
          ) : (
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-civic-700 mb-2">
                  Latitude
                </label>
                <input
                  type="number"
                  step="any"
                  value={manualLat}
                  onChange={(e) => setManualLat(e.target.value)}
                  placeholder="e.g., 40.7128"
                  className="input-field"
                  disabled={disabled}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-civic-700 mb-2">
                  Longitude
                </label>
                <input
                  type="number"
                  step="any"
                  value={manualLng}
                  onChange={(e) => setManualLng(e.target.value)}
                  placeholder="e.g., -74.0060"
                  className="input-field"
                  disabled={disabled}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-civic-700 mb-2">
                  Address (optional)
                </label>
                <input
                  type="text"
                  value={address}
                  onChange={(e) => setAddress(e.target.value)}
                  placeholder="e.g., Main Street, City"
                  className="input-field"
                  disabled={disabled}
                />
              </div>
              <button
                onClick={handleManualSubmit}
                disabled={disabled}
                className="btn-primary w-full"
              >
                Set Location
              </button>
            </div>
          )}
        </>
      ) : (
        <div className="bg-civic-100 rounded-lg p-4 space-y-2">
          <div className="flex items-center space-x-2 text-civic-700">
            <MapPin className="w-5 h-5" />
            <div>
              <p className="font-medium">{location.address}</p>
              <p className="text-sm text-civic-600">
                {location.lat.toFixed(6)}, {location.lng.toFixed(6)}
              </p>
            </div>
          </div>
          <div className="flex space-x-2">
            <button
              onClick={handleConfirm}
              disabled={disabled}
              className="btn-primary flex-1"
            >
              Confirm Location
            </button>
            <button
              onClick={() => {
                setLocation(null)
                setManualMode(false)
                setManualLat('')
                setManualLng('')
                setAddress('')
              }}
              disabled={disabled}
              className="btn-secondary"
            >
              Change
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

export default LocationPicker


