import { MapPin, Shield } from 'lucide-react'

function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-civic-200">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="bg-primary-600 p-2 rounded-lg">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold text-civic-900">Road Damage Reporter</h1>
              <p className="text-sm text-civic-600">Smart City Civic Platform</p>
            </div>
          </div>
          <div className="flex items-center space-x-2 text-civic-600">
            <MapPin className="w-5 h-5" />
            <span className="text-sm">SDG 11 Initiative</span>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header


