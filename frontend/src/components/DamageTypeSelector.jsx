import { AlertTriangle, Split, Wrench } from 'lucide-react'

const damageTypes = [
  { id: 'pothole', label: 'Pothole', icon: AlertTriangle, description: 'Hole or depression in the road surface' },
  { id: 'crack', label: 'Crack', icon: Split, description: 'Fracture or fissure in the road' },
  { id: 'surface_damage', label: 'Surface Damage', icon: Wrench, description: 'General surface deterioration or wear' },
  { id: 'other', label: 'Other', icon: AlertTriangle, description: 'Other type of road damage' }
]

function DamageTypeSelector({ onSelect, disabled }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
      {damageTypes.map((type) => {
        const Icon = type.icon
        return (
          <button
            key={type.id}
            onClick={() => onSelect(type.id)}
            disabled={disabled}
            className="bg-white border-2 border-civic-200 rounded-lg p-4 hover:border-primary-500 hover:bg-primary-50 transition-all text-left disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <div className="flex items-start space-x-3">
              <div className="bg-primary-100 p-2 rounded-lg">
                <Icon className="w-6 h-6 text-primary-600" />
              </div>
              <div>
                <h3 className="font-semibold text-civic-900">{type.label}</h3>
                <p className="text-sm text-civic-600 mt-1">{type.description}</p>
              </div>
            </div>
          </button>
        )
      })}
    </div>
  )
}

export default DamageTypeSelector


